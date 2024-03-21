

// // worker.js
let schedules = []

self.onmessage = function(event) {
    schedules = []
    const courses = event.data.courses;
    const emptysched = new Schedule()
    depthFirstSearch(courses, emptysched)
    self.postMessage({
        schedules: schedules
    });
};
const dayToIndex = {'M' : 0, 'T' : 1, 'W' : 2, 'R' : 3, 'F' : 4}
class Schedule {
    constructor(oldSched = null, section = null, index = null){
        if(oldSched == null){
            this.selectedOptions = []
            this.takenTimes = [[],[],[],[],[]]
        }
        else{
            this.selectedOptions = [...oldSched.selectedOptions]
            this.selectedOptions.push(index)
            this.takenTimes = [...oldSched.takenTimes]
           
        }
        
    }
}

function validEntry(currentSchedule, newLecture){
    const lecStart = newLecture.lecture.start
    const lecEnd = newLecture.lecture.end
    for(day in newLecture.lecture.days){
        const index = dayToIndex[day]
        for(time in currentSchedule.takenTimes[index]){
            // if the new lecture starts before the current lecture ends and ends after the current lecture starts
            if(time[1] >= lecStart && time[0] <= lecStart){
                return false
            }
            // if the new lecture starts before the current lecture ends and ends after the current lecture starts
            if(time[0] <= lecEnd && time[1] >= lecEnd){
                return false
            }
        }
    }
    if(newLecture.tutorial.start){
        const tutStart = newLecture.tutorial.start
        const tutEnd = newLecture.tutorial.end
        for(day in newLecture.tutorial.days){
            const index = dayToIndex[day]
            for(time in currentSchedule.takenTimes[index]){
                // if the new lecture starts before the current lecture ends and ends after the current lecture starts
                if(time[1] > tutStart && time[0] < tutStart){
                    return false
                }
                // if the new lecture starts before the current lecture ends and ends after the current lecture starts
                if(time[0] < tutEnd && time[1] > tutEnd){
                    return false
                }
            }
        }
    }
    return true
}

function depthFirstSearch(remainingCourses, currentSchedule){
    if (remainingCourses.length === 0) {
        schedules.push(currentSchedule.selectedOptions.slice()); // Create copy
        return;
    }
    const course = remainingCourses[remainingCourses.length - 1]
    const newRemainingCourses = remainingCourses.slice(0, remainingCourses.length - 1);
    // Todo pick course based on heurstic
    for(let index = 0; index < course.selectedIndices.length; index++){
        const section = course.combinations[index]
        if(!course.selectedIndices[index]){
            continue
        }
        const lectureInfo = {
            lecture: {
                start: null,
                end: null,
                days: null,
            },
            tutorial: {
                start: null,
                end: null,
                days: null,
            },
            
        }
        for(let i = 0; i < course.lectures.length; i++){
            if(course.lectures[i].name == section[0]){
                lectureInfo.lecture.start = course.lectures[i].start
                lectureInfo.lecture.end = course.lectures[i].end
                lectureInfo.lecture.days = course.lectures[i].days
            }
        }
        if(section.length > 1){
            for(let i = 0; i < course.tutorials.length; i++){
                if(course.tutorials[i].name == section[1]){
                    lectureInfo.tutorial.start = course.tutorials[i].start
                    lectureInfo.tutorial.end = course.tutorials[i].end
                    lectureInfo.tutorial.days = course.tutorials[i].days
                }
            }
        }
        if(validEntry(currentSchedule, lectureInfo)){
            currentSchedule.selectedOptions.push(index);
            for(let i = 0; i < section.lecture.days.length; i++){
                const day = section.lecture.days[i]
                const index = dayToIndex[day]
                this.takenTimes[index].push([section.lecture.start, section.lecture.end])
               
            }
            if(section.tutorial.start){
                for(let i = 0; i < section.tutorial.days.length; i++){
                    const day = section.tutorial.days[i]
                    const index = dayToIndex[day]
                    this.takenTimes[index].push([section.tutorial.start, section.tutorial.end])
                }
            }
            {
                depthFirstSearch(newRemainingCourses, currentSchedule)
                currentSchedule.selectedOptions.pop(); 
                for(let i = 0; i < section.lecture.days.length; i++){
                    const day = section.lecture.days[i]
                    const index = dayToIndex[day]
                    this.takenTimes[index].pop()
                }
                if(section.tutorial.start){
                    for(let i = 0; i < section.tutorial.days.length; i++){
                        const day = section.tutorial.days[i]
                        const index = dayToIndex[day]
                        this.takenTimes[index].pop()
                    }
                }
            }
        }
    }
    
}
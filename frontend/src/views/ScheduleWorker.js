// worker.js
let schedules = []
self.onmessage = function(event) {
    schedules = []

    const combinations = event.data;
    
    // Send a message back to the main thread
    self.postMessage('Message from web worker');
};

currentSchedule = {
    currentSchedule: {

    },
    takenTimes: [[],[],[],[],[]]
}

function validEntry(currentSchedule, newLecture){

}

function addEntry(){

}

function convertLectureOption(course, key){
    const lecture = course.lecture[key[0]];
    const lab = course.lab[key[1]];
    const tutorial = course.tutorial[key[2]];
}

function heursticSort(){

}

function depthFirstSearch(remainingCourses, currentSchedule, schedules){
    course = remainingCourses[remainingCourses.length - 1]
    for(lecture in course.combos){
        if(validEntry(currentSchedule, lecture)){
            const newSchedule = addEntry(currentSchedule, lecture)
            if(remainingCourses.length == 1){
                delete newSchedule.takenTimes
                schedules.push(convertScheduleBack(newSchedule))
            }
            else{
                const newRemainingCourses = remainingCourses.slice(0, remainingCourses.length - 1);
                depthFirstSearch(newRemainingCourses, currentSchedule, schedules)
            }
        }
    }
    
}
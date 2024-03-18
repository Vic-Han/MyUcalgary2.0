<template>
    <div class="academic-report bg-grey-100 shadow-inner p-4 ">
      <div class="flex flex-row">
        <div class="program-information bg-white shadow-md rounded-lg p-6 mb-4 bg-white-100 w-2/5 text-start">
          <h1 class="text-xl font-semibold mb-4">Program Information</h1>
          <p><strong>Degree Stream:</strong> {{ programInfo.degree }}</p>
          <p><strong>Major:</strong> {{ programInfo.major }}</p>
          <p><strong>Minor:</strong> {{ programInfo.minor }}</p>
          <p><strong>Concentration:</strong> {{ programInfo.concentrartion }}</p>
          <p><strong>Year of Program:</strong> {{ programInfo.Year }}</p>
          <p><strong>Academic Load:</strong> {{ programInfo.academicLoad }}</p>
        </div>
        <div class="bg-white-100 rounded-lg shadow-md px-6 mb-4 ml-4 w-3/5">
          <div class="text-left font-semibold text-xl pt-6">Degree Progress</div>
          <div class="w-full h-10 bg-grey-100 shadow-xl mt-10 rounded-lg"></div>
          <div class="absolute -translate-y-20 w-16 h-10 bg-green-100 mt-10 rounded-lg">
            <div class="pt-1 text-2xl text-white-100 font-semibold">{{ completedProgress }}%</div>
          </div>
          <div class="flex flex-row mt-2">
            <div class="w-1/3 text-lg font-semibold text-left">0%</div>
            <div class="w-1/3 text-lg font-semibold">50%</div>
            <div class="w-1/3 text-lg font-semibold text-right">100%</div>
          </div>
        </div>
      </div>
      <div class="h-2/3 w-full bg-white-100 rounded-xl shadow-xl p-6">
        <div class="font-semibold text-2xl text-left pb-4">Course Breakdown</div>
        <div class="overflow-y-auto max-h-2/3">
          <div v-for="(Requirement,index) in requiredCourses" :key="index">
            <div class="flex flex-row">
              <div class="text-left font-semibold text-l w-fit">{{ Requirement.description }}:</div>
              <div v-if="Requirement.status =='complete'" class="flex flex-row items-center pl-6">
                <div>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-green-100" viewBox="0 -960 960 960">
                    <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                  </svg>
                </div>
                <div class="pl-2 text-sm italic text-green-100">Complete</div>
              </div>
            </div>
            <div v-if="index == 0" class="grid grid-cols-1">
              <div v-for="(semester,i) in Requirement.courses">
                <div class="font-semibold">{{ semester.year }}</div>
                <div class="grid grid-cols-5 gap-4">
                  <div v-for="(course,j) in semester.fall">
                    <div>
                      {{ course.name }}
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-5 gap-4 pt-2">
                  <div v-for="(course,j) in semester.winter">
                    <div>
                      {{ course.name }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Academic Report Details -->
      <!-- <div class="academic-report-details bg-white shadow-md rounded-lg p-6 mb-6 bg-white-100 overflow-x-hidden" :class="{ 'overflow-hidden': !expandedReport, 'overflow-auto h-full': expandedReport }">
        <h2 class="text-xl font-semibold mb-4">Academic Report</h2> -->
      
        <!-- Major Field -->
        <!-- <div class="font-semibold col-span-full">Major Field</div>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-4">
          <template v-for="(course, index) in incompleteMajorField" :key="`major-${index}`">
            <div class="course-item relative group" 
              @mouseenter="course.hovered = true" 
              @mouseleave="course.hovered = false"> -->
              <!-- Course box -->
              <!-- <div :class="{
                'bg-green-200': course.status === 'completed',
                'bg-yellow-200': course.status === 'in-progress',
                'bg-white-100 border border-grey-100': course.status === 'incomplete',
                'p-2': true,
                'rounded': true,
                'shadow': true,
                'text-center': true
              }" class="hover:-translate-y-1 transition-transform duration-300">
                {{ course.code }}
              </div> -->
              <!-- Tooltip -->
              <!-- <div v-if="course.hovered" class="tooltip absolute bottom-full mb-2 -translate-x-1/2 left-1/2 text-black p-2 border border-gray-500 bg-white-100 rounded shadow-lg whitespace-nowrap max-w-screen overflow-x-auto z-10">
                <div><strong>Description:</strong> {{ course.description }}</div>
                <div><strong>Units:</strong> {{ course.units }}</div>
                <div><strong>Semester:</strong> {{ course.semester }}</div>
                <div><strong>Grade:</strong> {{ course.grade }}</div>
              </div>
            </div>
          </template>
        </div> -->

        <!-- Required Options -->
        <!-- <div class="flex flex-col my-4 gap-y-4">
            <div v-for="(option, index) in requiredOptions" :key="index">
              <h3 class="font-semibold">{{ option.name }}</h3>
              <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <template v-for="(course, index) in option.courses" :key="`major-${index}`">
                  <div class="course-item relative group" 
                    @mouseenter="course.hovered = true" 
                    @mouseleave="course.hovered = false"> -->
                    <!-- Course box -->
                    <!-- <div :class="{
                      'bg-green-200': course.status === 'completed',
                      'bg-yellow-200': course.status === 'in-progress',
                      'bg-white-100 border border-grey-100' : course.status === 'incomplete',
                      'p-2': true,
                      'rounded': true,
                      'shadow': true,
                      'text-center': true
                    }" class="hover:-translate-y-1 transition-transform duration-300">
                      {{ course.code }}
                    </div> -->
                    <!-- Tooltip -->
                    <!-- <div v-if="course.hovered" class="tooltip absolute bottom-full mb-2 -translate-x-1/2 left-1/2 text-black p-2 border border-gray-500 bg-white-100 rounded shadow-lg whitespace-nowrap max-w-screen overflow-x-auto z-10">
                      <div><strong>Description:</strong> {{ course.description }}</div>
                      <div><strong>Units:</strong> {{ course.units }}</div>
                      <div><strong>Semester:</strong> {{ course.semester }}</div>
                      <div><strong>Grade:</strong> {{ course.grade }}</div>
                    </div>
                  </div>
                </template>
              </div>
            </div>
        </div> -->
<!-- 
      </div> -->

      <!-- <div class="flex justify-center mt-4">
          <button class="btn bg-gray-100 py-2 px-4 rounded transition-colors flex items-center justify-center gap-2" @click="toggleExpandedReport">
            <span v-if="expandedReport" class="text-lg transform rotate-[-90deg] text-black-100">&#8250;</span>
            <span v-else class="text-lg transform rotate-[90deg] text-black-100">&#8250;</span>
          </button>
        </div> -->
    </div>
  </template>
  
  
<script>
  export default {
    name: 'AcademicReport',
    emits: ['show-navbar', 'set-title'],
    data: ()=> {
      return {

        expandedReport: false,
        completedProgress: 0,
        pendingProgress:0,
        programInfo: {
          degree: "Bachelor of Science",
          major: "Software Engineering Internship Designation",
          minor: "None",
          concentrartion: 'None',
          Year: 6,
          academicLoad: "Full-Time"
        },
        requiredCourses:
        [
          
        ]
           
        // requiredCourses: {
        //     status: 'incomplete',
        //     courses: [
        //       { code: 'CPSC 231', status: 'completed', description: 'Introduction to Computer Science', units: 3, semester: 'Fall 2020', grade: 'A+', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 233', status: 'completed', description: 'Principles of Software Design', units: 3, semester: 'Winter 2021', grade: 'A', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 331', status: 'completed', description: 'Data Structures, Algorithms, and Their Analysis', units: 3, semester: 'Spring 2021', grade: 'B+', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 313', status: 'completed', description: 'Computer Hardware and Operating Systems', units: 3, semester: 'Fall 2021', grade: 'B', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 449', status: 'in-progress', description: 'Advanced Programming Techniques', units: 3, semester: 'Winter 2022', grade: 'in-progress', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 457', status: 'in-progress', description: 'Principles of Operating Systems', units: 3, semester: 'Winter 2022', grade: 'in-progress', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 471', status: 'incomplete', description: 'Database Systems', units: 3, semester: 'To Be Taken', grade: 'N/A', hovered: false, type: 'majorReq' },
        //       { code: 'CPSC 481', status: 'incomplete', description: 'Human-Computer Interaction I', units: 3, semester: 'To Be Taken', grade: 'N/A', hovered: false, type: 'majorReq' },
        //     ]
        // },

        // requiredOptions: [
        //   {
        //     name: '500+ level',
        //     status: 'in-progress',
        //     courses: [
        //     { code: 'CPSC 533', status: 'completed' },
        //     { code: 'CPSC 535', status: 'completed' },
        //     { code: 'CPSC 537', status: 'in-progress' },
        //     ]
        //   },
        //   {
        //     name: '400+ level',
        //     status: 'incomplete',
        //     courses: [
        //     { code: 'CPSC 541', status: 'in-progress' },
        //     { code: 'CPSC 453', status: 'completed' },
        //     { code: 'CPSC 457', status: 'completed' },
        //     { code: 'CPSC 471', status: 'in-progress' },
        //     ]
        //   },
        //   {
        //     name: '300+ level',
        //     status: 'completed',
        //     courses: [
        //     { code: 'CPSC 319', status: 'in-progress' },
        //     { code: 'CPSC 355', status: 'completed' },
        //     ]
        //   },
        // ],
      }
    },
    computed: {
        incompleteMajorField() {
            if (this.expandedReport) {
                return this.requiredCourses.courses.filter(course => course.status === 'incomplete' || course.status === 'in-progress' || course.status === 'completed');
                
            } else {
                return this.requiredCourses.courses.filter(course => course.status === 'incomplete');
            }
        },

        incompleteOptions() {
            if (this.expandedReport) {
                return this.requiredOptions.map(option => ({...option,
                courses: option.courses.filter(course => course.status === 'incomplete' || course.status === 'in-progress' || course.status === 'completed')}));
            } else {
                return this.requiredOptions.map(option => ({...option,
                courses: option.courses.filter(course => course.status === 'incomplete')}));
            }
        },
    
      canApplyForGraduation() {
        // Logic to determine if the student can apply for graduation
        return this.academicReport.programs.some(program => {
          return program.unitsNeeded === 0;
        });
      },
      completedCoursesReport() {
        return this.academicReport.programs.map(program => {
        const updatedProgram = { ...program };
        updatedProgram.courseCategory = program.courseCategory.map(category => {
            const updatedCategory = { ...category };
            updatedCategory.courseField = category.courseField.map(field => {
            const updatedField = { ...field };
            updatedField.courses = field.courses.filter(course => course.status === 'complete');
            return updatedField;
            });
            return updatedCategory;
        });
        return updatedProgram;
        });
      },
      programUnits() {
        // Check if `academicReport` and `programs` are defined and if they are arrays.
        if (!this.academicReport || !Array.isArray(this.academicReport.programs)) {
        return []; // Return an empty array if not defined or not an array
        }

        return this.academicReport.programs.map(program => {
        // Start with zero units taken and then sum up based on course status
        let unitsTaken = 0;

        // Check if `courseCategory` exists and is an array before iterating over it
        if (Array.isArray(program.courseCategory)) {
            program.courseCategory.forEach(category => {
            // Check if `courseField` exists and is an array before iterating over it
            if (Array.isArray(category.courseField)) {
                category.courseField.forEach(field => {
                field.courses.forEach(course => {
                    if (course.status === 'complete' || course.status === 'incomplete') {
                    unitsTaken = unitsTaken + 3; // Assuming each course is worth one unit
                    }
                });
                });
            }
            });
        }

        // Calculate units needed based on the units taken
        const unitsNeeded = Math.max(program.unitsRequired - unitsTaken, 0); // Ensure it doesn't go below zero

        // Return an object with the computed units information for the program
        return {
            ...program,
            unitsTaken,
            unitsNeeded
        };
        });
    }
    },
    methods: {
        toggleExpandedReport() {
            this.expandedReport = !this.expandedReport;
        },
        toggleReportDetails(index) {
            const program = this.academicReport.programs[index];
            // Ensure program exists and has courseCategory defined
            if (program && Array.isArray(program.courseCategory)) {
            program.isExpanded = !program.isExpanded;
            if (!program.isExpanded) {
                // Store full course list if not done already
                if (!program.fullCourseList) {
                program.fullCourseList = program.courseCategory.map(category => ({
                    ...category, 
                    courseField: category.courseField.map(field => ({ ...field }))
                }));
                }
                // Filter out completed and inProgress courses
                program.courseCategory.forEach(category => {
                category.courseField.forEach(field => {
                    field.courses = field.courses.filter(course => course.status === 'incomplete');
                });
                });
            } else {
                // Restore the full course list if it has been stored
                if (program.fullCourseList) {
                program.courseCategory = program.fullCourseList.map(category => ({
                    ...category, 
                    courseField: category.courseField.map(field => ({ ...field }))
                }));
                }
            }
            } else {
            console.error('Program or courseCategory is undefined.');
            }
        },
        toggleAllReports() {
            this.areAllReportsExpanded = !this.areAllReportsExpanded;
            this.academicReport.programs.forEach((program, index) => {
            // Toggle the expanded state for each program
            this.toggleReportDetails(index);
            });

        }
    },
    created() {
      this.$emit('show-navbar')
      this.$emit('toggle-selected','academics')

      function filterSemester(course, predicate) {
        return course.semester == predicate
      }

      const backendData = {
        "requirements":
        [
            {
                "description": "Required Courses",
                "requiredUnits": 96,
                "status": "in-progress",
                "courses":
                [
                    {
                        "name": "CHEM209",
                        "units": 3,
                        "status": "complete",
                        "semester": "F1"
                    },
                    {
                        "name": "ENGG233",
                        "units": 3,
                        "status": "complete",
                        "semester": "F1"
                    },
                    {
                        "name": "MATH275",
                        "units": 3,
                        "status": "complete",
                        "semester": "F1"
                    },
                    {
                        "name": "MATH211",
                        "units": 3,
                        "status": "complete",
                        "semester": "F1"
                    },
                    {
                        "name": "ENGG225",
                        "units": 3,
                        "status": "complete",
                        "semester": "F1"
                    },
                    {
                        "name": "ENGG201",
                        "units": 3,
                        "status": "complete",
                        "semester": "W1"
                    },
                    {
                        "name": "ENGG202",
                        "units": 3,
                        "status": "complete",
                        "semester": "W1"
                    },
                    {
                        "name": "MATH277",
                        "units": 3,
                        "status": "complete",
                        "semester": "W1"
                    },
                    {
                        "name": "PHYS259",
                        "units": 3,
                        "status": "complete",
                        "semester": "W1"
                    },
                    {
                        "name": "ENGG200",
                        "units": 3,
                        "status": "complete",
                        "semester": "W1"
                    },
                    {
                        "name": "ENGG319",
                        "units": 3,
                        "status": "complete",
                        "semester": "F2"
                    },
                    {
                        "name": "PHYS365",
                        "units": 3,
                        "status": "complete",
                        "semester": "F2"
                    },
                    {
                        "name": "MATH375",
                        "units": 3,
                        "status": "complete",
                        "semester": "F2"
                    },
                    {
                        "name": "ENSF337",
                        "units": 3,
                        "status": "complete",
                        "semester": "F2"
                    },
                    {
                        "name": "ENEL353",
                        "units": 3,
                        "status": "complete",
                        "semester": "F2"
                    },
                    {
                        "name": "MATH271",
                        "units": 3,
                        "status": "complete",
                        "semester": "W2"
                    },
                    {
                        "name": "ENEL327",
                        "units": 3,
                        "status": "complete",
                        "semester": "W2"
                    },
                    {
                        "name": "ENSF409",
                        "units": 3,
                        "status": "complete",
                        "semester": "W2"
                    },
                    {
                        "name": "ENCM369",
                        "units": 3,
                        "status": "complete",
                        "semester": "W2"
                    },
                    {
                        "name": "CPSC319",
                        "units": 3,
                        "status": "complete",
                        "semester": "W2"
                    },
                    {
                        "name": "ENSF480",
                        "units": 3,
                        "status": "complete",
                        "semester": "F3"
                    },
                    {
                        "name": "ENCM511",
                        "units": 3,
                        "status": "complete",
                        "semester": "F3"
                    },
                    {
                        "name": "CPSC457",
                        "units": 3,
                        "status": "complete",
                        "semester": "F3"
                    },
                    {
                        "name": "SENG401",
                        "units": 3,
                        "status": "in-progress",
                        "semester": "W3"
                    },
                    {
                        "name": "SENG438",
                        "units": 3,
                        "status": "in-progress",
                        "semester": "W3"
                    },
                    {
                        "name": "SENG471",
                        "units": 3,
                        "status": "in-progress",
                        "semester": "W3"
                    },
                    {
                        "name": "CPSC441",
                        "units": 3,
                        "status": "complete",
                        "semester": "W3"
                    },
                    {
                        "name": "CPSC471",
                        "units": 3,
                        "status": "complete",
                        "semester": "W3"
                    },
                    {
                        "name": "CPSC471",
                        "units": 3,
                        "status": "complete",
                        "semester": "W3"
                    },
                    {
                        "name": "ENEL500A",
                        "units": 3,
                        "status": "incomplete",
                        "semester": "F4"
                    },
                    {
                        "name": "SENG511",
                        "units": 3,
                        "status": "complete",
                        "semester": "F4"
                    },
                    {
                        "name": "ENEL500B",
                        "units": 3,
                        "status": "incomplete",
                        "semester": "W4"
                    },
                    {
                        "name": "SENG533",
                        "units": 3,
                        "status": "complete",
                        "semester": "W4"
                    },
                ]
            },
            {
                "description": "Technical Electives",
                "requiredUnits": 6,
                "status": "complete",
                "courses":
                [
                    {
                        "name": "SENG550",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "SENG567",
                        "units": 3,
                        "status": "incomplete"
                    },
                    {
                        "name": "SENG512",
                        "units": 3,
                        "status": "incomplete"
                    },
                    {
                        "name": "SENG570",
                        "units": 3,
                        "status": "incomplete"
                    },
                    {
                        "name": "SENG580",
                        "units": 3,
                        "status": "incomplete"
                    }
                ]
            },
            {
                "description": "Complementary Studies",
                "requiredUnits": 18,
                "status": "in-progress",
                "courses":
                [
                    {
                        "name": "ECON201",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "ECON203",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "ENGG209",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "COMS363",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "ENGG481",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "ENGG513",
                        "units": 3,
                        "status": "incomplete"
                    },
                ]
            },
            {
                "description": "Internship designation",
                "requiredUnits": 9,
                "status": "complete",
                "courses":
                [
                    {
                        "name": "INTE513.1",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "INTE513.2",
                        "units": 3,
                        "status": "complete"
                    },
                    {
                        "name": "INTE513.3",
                        "units": 3,
                        "status": "complete"
                    }
                ]
            }
        ]
      } 
      let totalUnits = 0
      let takenUnits = 0
      let pendingUnits = 0
      this.requiredCourses.push({
        description: backendData.requirements[0].description,
        requiredUnits: backendData.requirements[0].requiredUnits,
        status: backendData.requirements[0].status,
        courses: [
          {
            year: "First Year",
            fall: backendData.requirements[0].courses.filter(course=> filterSemester(course, "F1")),
            winter: backendData.requirements[0].courses.filter(course=> filterSemester(course, "W1"))
          },
          {
            year: "Second Year",
            fall: backendData.requirements[0].courses.filter(course=> filterSemester(course, "F2")),
            winter: backendData.requirements[0].courses.filter(course=> filterSemester(course, "W2"))
          },
          {
            year: "Third Year",
            fall: backendData.requirements[0].courses.filter(course=> filterSemester(course, "F3")),
            winter: backendData.requirements[0].courses.filter(course=> filterSemester(course, "W3"))
          },
          {
            year: "Fourth Year",
            fall: backendData.requirements[0].courses.filter(course=> filterSemester(course, "F4")),
            winter: backendData.requirements[0].courses.filter(course=> filterSemester(course, "W4"))
          }
        ]
      })
      for(let i = 0; i<backendData.requirements[0].courses.length; i++){
        if(backendData.requirements[0].courses[i].status == 'complete') {
          takenUnits += backendData.requirements[0].courses[i].units 
        }
        if(backendData.requirements[0].courses[i].status == 'in-progress') {
          pendingUnits += backendData.requirements[0].courses[i].units 
        }
      }
      totalUnits += backendData.requirements[0].requiredUnits
      for(let i = 1; i < backendData.requirements.length; i++) {
        totalUnits += backendData.requirements[i].requiredUnits
        const requiredCourseNos = backendData.requirements[i].requiredUnits / 3
        this.requiredCourses.push({
          description: backendData.requirements[i].description,
          requiredUnits: backendData.requirements[i].requiredUnits,
          status: backendData.requirements[i].status,
          courses: []
        })
        for(let j = 0; j < requiredCourseNos; j++) {
          if(backendData.requirements[i].courses[j].status == 'complete') {
            takenUnits += backendData.requirements[i].courses[j].units
            this.requiredCourses[i].courses.push(backendData.requirements[i].courses[j])
          }
          if(backendData.requirements[i].courses[j].status == 'in-progress') {
            pendingUnits += backendData.requirements[i].courses[j].units
            this.requiredCourses[i].courses.push(backendData.requirements[i].courses[j])
          }
          if(backendData.requirements[i].courses[j].status == 'incomplete') {
            this.requiredCourses[i].courses.push({
              name: "Option",
              units: 3,
              status: "incomplete"
            })
          }
        }
      }
      this.completedProgress = Math.round((takenUnits/totalUnits)*100)
      this.pendingProgress = Math.round((pendingUnits/totalUnits)*100)
      // Preset data should not be modified here, it should be set in data() or computed
    }
  }
</script>
    
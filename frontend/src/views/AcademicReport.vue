<template>
    <div class="academic-report bg-gray-100 p-4">
      <div class="program-information bg-white shadow-md rounded-lg p-6 mb-6">
        <h1 class="text-xl font-semibold mb-4">Program Information</h1>
        <p><strong>Degree Stream:</strong> {{ programInfo.degreeStream }}</p>
        <p><strong>Major:</strong> {{ programInfo.major }}</p>
        <p><strong>Year of Program:</strong> {{ programInfo.yearOfProgram }}</p>
        <p><strong>Academic Load:</strong> {{ programInfo.academicLoad }}</p>
      </div>
  
      <div class="academic-report-details bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 class="text-xl font-semibold mb-4">Academic Report</h2>
        <div v-for="(report, index) in academicReport.programs" :key="index">
        <div class="report-summary">
            <h3 class="font-semibold cursor-pointer" @click="toggleReportDetails(index)">
                {{ report.programName }}
                <span>{{ report.isExpanded ? '−' : '+' }}</span>
                </h3>
                <div v-if="report.isExpanded">
                <div v-for="(program, index) in programUnits" :key="index">
                    <h3>{{ program.programName }}</h3>
                    <p>Units {{ program.unitsRequired }} required, {{ program.unitsTaken }} taken, {{ program.unitsNeeded }} needed</p>
                </div>
                <div v-for="category in report.courseCategory" :key="category.categoryName">
                    <p class="font-semibold">{{ category.categoryName }}</p>
                    <div v-for="field in category.courseField" :key="field.fieldName" class="mb-4">
                    <p class="font-semibold">{{ field.fieldName }}</p>
                    <div class="flex flex-wrap gap-2">
                        <div v-for="course in field.courses" :key="course.code" class="relative group">
                            <div :class="{
                                    'bg-[#A9DD91] shadow': course.status === 'complete',
                                    'bg-[#EBEB71] shadow': course.status === 'inProgress',
                                    'bg-[#FFFFFF] shadow': course.status === 'incomplete',
                                }"
                                @mouseenter="course.hovered = true" 
                                @mouseleave="course.hovered = false"
                                class="rounded-md text-center px-6 py-1 text-sm border border-gray-500 font-medium hover:-translate-y-1 transition-transform duration-300 cursor-pointer">
                                {{ course.code }}
                            </div>
                            <div v-if="course.hovered" class="absolute bottom-full mb-2 left-1/2 transform -translate-x-1/2 bg-white text-black p-2 border border-gray-500 rounded shadow-lg" style="background-color: white; opacity: 1; white-space: nowrap; max-width: 100vw; overflow-x: auto;">
                                <div><strong>Description:</strong> {{ course.description }}</div>
                                <div><strong>Units:</strong> {{ course.units }}</div>
                                <div><strong>Semester:</strong> {{ course.semester }}</div>
                                <div><strong>Grade:</strong> {{ course.grade }}</div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <button class="btn bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors" @click="toggleAllReports">
          {{ areAllReportsExpanded ? 'Hide Full Reports' : 'Show Full Reports' }}
        </button>
      </div>
  </template>
  
<script>
  export default {
    name: 'AcademicReport',
    data() {
      return {
        programInfo: {
          degreeStream: "Bachelor of Science",
          major: "Computer Science",
          minor: "None",
          concentration: "None",
          yearOfProgram: 4,
          academicLoad: "Full-Time"
        },
        academicReport: {
          programs: [
            {
              programName: "BSC in Computer Science",
              unitsRequired: 120.00,
              unitsTaken: 114.00,
              unitsNeeded: 6.00,
              courseCategory: [
                {
                    categoryName: 'Required Courses',
                    courseField: [
                    {
                        fieldName: 'Major Field',
                        courses: [
                        { code: 'CPSC 231', status: 'complete', description: 'Introduction to Computer Science', units: 3, semester: 'Fall 2020', grade: 'A+', hovered: false },
                        { code: 'CPSC 233', status: 'complete' },
                        { code: 'CPSC 251', status: 'complete' },
                        { code: 'CPSC 351', status: 'complete' },
                        { code: 'CPSC 355', status: 'complete' },
                        { code: 'CPSC 413', status: 'complete' },
                        { code: 'CPSC 449', status: 'complete' },
                        { code: 'CPSC 457', status: 'complete' },
                        { code: 'CPSC 331', status: 'incomplete' },
                        { code: 'SENG 300', status: 'incomplete' },
                        { code: 'CPSC 581', status: 'complete' },
                        { code: 'SENG 511', status: 'complete' },
                        { code: 'SENG 513', status: 'inProgress' },
                        { code: 'CPSC 471', status: 'complete' },
                        { code: 'CPSC 481', status: 'complete' },
                        { code: 'CPSC 573', status: 'complete' },
                        { code: 'SENG 401', status: 'inProgress' },
                        { code: 'CPSC 329', status: 'complete' },
                        { code: 'CPSC 359', status: 'complete' },
                        { code: 'SENG 550', status: 'complete' }
                        ]
                    },
                    {
                        fieldName: 'Math',
                        courses: [
                        { code: 'MATH 265', status: 'complete' },
                        { code: 'MATH 211', status: 'complete' }
                        ]
                    },
                    {
                        fieldName: 'Logic',
                        courses: [
                        { code: 'PHIL 279', status: 'complete' }
                        ]
                    },
                    {
                        fieldName: 'Ethics',
                        courses: [
                        { code: 'PHIL 314', status: 'incomplete' }
                        ]
                    }
                    ]
                },
                {
                    categoryName: 'Breadth Requirements',
                    courseField: [
                    {
                        courses: [
                        { code: 'ECON 201', status: 'complete' },
                        { code: 'GRST 211', status: 'complete' },
                        { code: 'DRAM 205', status: 'complete' }
                        ]
                    }
                    ]
                },
                {
                    categoryName: 'Open Options',
                    courseField: [
                    {
                        fieldName: 'Non-Major Field',
                        courses: [
                        { code: 'MATH 267', status: 'complete' },
                        { code: 'STAT 321', status: 'complete' },
                        { code: 'STAT 323', status: 'complete' },
                        { code: 'DATA 201', status: 'complete' },
                        { code: 'SOCI 201', status: 'complete' },
                        { code: 'ANTH 201', status: 'complete' },
                        { code: 'FILM 201', status: 'complete' },
                        { code: 'GLGY 305', status: 'incomplete' },
                        // '+ 6 Units' 
                        ]
                    },
                    {
                        fieldName: 'Open Options',
                        courses: [
                        { code: 'CPSC 441', status: 'complete' },
                        { code: 'CPSC 491', status: 'complete' }
                        ]
                    }
                    ]
                }
                ],
              isExpanded: false,
              fullCourseList: null,
              // Add breadth requirements and open options similarly
            },
            {
              programName: "Minor in Architecture",
              // Other details for this program
              isExpanded: false,
              fullCourseList: null,
            }
            // Add more programs if needed
          ]
        },
        areAllReportsExpanded: false,
      }
    },
    computed: {
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
      this.$emit('show-search')
      this.$emit('show-profile')
      this.$emit('set-title','Academic Report')
      // Preset data should not be modified here, it should be set in data() or computed
    }
  }
</script>
    
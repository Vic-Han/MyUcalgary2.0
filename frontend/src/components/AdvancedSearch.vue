<template>
    <div class = "fixed w-screen h-screen z-30 opacity-50 bg-black-100"></div>
    <div class = "fixed w-1/3 h-96 z-40 bg-white-100 rounded-xl left-1/2 -translate-x-1/2 top-1/3 -translate-y-1/2">
        <div @click="closeAdvancedSearch"> Close </div>
        <form class="bg-white-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <!-- Requirement Type -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-gray-700 text-xl mb-2 mr-2" for="requirement-type">
                Requirement Type
            </label>
            <div class="relative">
            <select v-model="selectedRequirementType" class="relative w-48 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-4 m-3 text-center">
                <option v-for="type in requirementTypes" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedRequirementType }">{{ type }}</option>
            </select>
            </div>
        </div>

        <!-- Faculty -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-gray-700 text-xl mb-2 mr-2" for="requirement-type">
                Faculty
            </label>
            <div class="relative">
            <select v-model="selectedFacultyType" class="relative w-48 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-4 m-3 text-center">
                <option v-for="type in facultyTypes" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedFacultyType }" class="">{{ type }}</option>
            </select>
            </div>
        </div>

        <!-- Major -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-gray-700 text-xl mb-2 mr-2" for="requirement-type">
                Major
            </label>
            <div class="relative">
            <select v-model="selectedMajorType" class="relative w-48 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-4 m-3 text-center">
                <option v-for="type in majorType" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedFacultyType }" class="">{{ type }}</option>
            </select>
            </div>
        </div>

        <!-- Course Number -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-gray-700 text-xl mb-2 mr-2" for="requirement-type">
                Course Number
            </label>
            <div class="flex">
            <select v-model="selectedEq" class="relative w-20 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-1 my-3 text-center">
                <option v-for="type in eqTypes" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedFacultyType }" class="">{{ type }}</option>
            </select>
            <input type="text" id="inputBox" v-model="courseInputValue" class="w-24 rounded-lg border-2 border-grey-200 focus:border-blue-500 py-2 px-2 m-3">
            </div>
        </div>

        <!-- Mode -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-gray-700 text-xl mb-2 mr-2" for="mode">
            Mode
            </label>
            <div class="">
                <div
                    :class="{
                    'bg-white-100  rounded-md h-112 w-48 py-2 px-1 my-3  cursor-pointer border-2 border-grey-200': true,
                    'bg-blue-500': isOnline,
                    }"
                    @click="toggleMode">
                    <div class="bg-white rounded-md h-8 w-1/2 left-1 shadow-md transition-transform duration-150 ease-in-out border-2 border-grey-200" :class="{ 'translate-x-full': !isOnline }">
                        <span class="text-sm text-gray-500">
                            {{ isOnline ? 'Online' : 'Offline' }}
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex items-center">
            <label class="block text-gray-700 text-xl mb-2 mr-2">Time</label>
            <div class="flex ml-auto">
                <input
                    type="text"
                    id="start-time"
                    placeholder="HH:MM"
                    class="w-24 px-3 py-2 text-center rounded-md border border-gray-300 focus:outline-none focus:ring-blue-500 focus:ring-1"
                    v-model="startTime"
                />
                <span class="flex items-center justify-between mx-2 text-xl">to</span>
                <input
                    type="text"
                    id="end-time"
                    placeholder="HH:MM"
                    class="w-24 px-3 py-2 text-center rounded-md border border-gray-300 focus:outline-none focus:ring-blue-500 focus:ring-1"
                    v-model="endTime"
                />
            </div>
        </div>

        <!-- Days of the week buttons -->
        <div class="mb-4">
          <label class="block text-gray-700 text-xl mb-2 mr-2 text-left" for="requirement-type">
            Days
          </label>
          <div class="flex space-x-2">
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" >Monday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow">Tuesday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow">Wednesday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow">Thursday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow">Friday</button>
          </div>
        </div>
  
        <!-- Search button -->
        <div class="flex items-center justify-center">
          <button class="bg-white-100 border-2 border-gray-400 hover:bg-gray-300 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Search
          </button>
        </div>
      </form>
    </div>
</template>  

<script>
    export default{
        name : 'AdvancedSearch',
        data : () => {
            return {
                selectedRequirementType: '',
                requirementTypes: ['general', 'major', 'breadth'],
                selectedFacultyType: '',
                facultyTypes: ['Engineering', 'Science', 'Arts', 'Business', 'Medicine', 'Nursing', 'Kinesiology', 'Education', 'Law', 'Social Work', 'Veterinary Medicine', 'Fine Arts', 'Music', 'Haskayne School of Business', 'Schulich School of Engineering', 'Faculty of Science', 'Faculty of Arts', 'Faculty of Nursing', 'Faculty of Kinesiology', 'Faculty of Education', 'Faculty of Law', 'Faculty of Social Work', 'Faculty of Veterinary Medicine', 'Faculty of Fine Arts', 'Faculty of Music'],
                selectedMajorType: '',
                majorType: ['Computer Science', 'Software Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Petroleum Engineering', 'Geological Engineering', 'Geomatics Engineering', 'Biomedical Engineering', 'Environmental Engineering', 'Engineering Physics', 'Aerospace Engineering', 'Materials Engineering', 'Mining Engineering', 'Oil and Gas Engineering', 'Energy Engineering', 'Sustainable Energy Engineering', 'Sustainable Systems Engineering', 'Sustainable Development Engineering', 'Sustainable Infrastructure Engineering', 'Sustainable Resources Engineering', 'Sustainable Environmental Engineering', 'Sustainable Chemical Engineering', 'Sustainable Petroleum Engineering', 'Sustainable Geological Engineering', 'Sustainable Geomatics Engineering', 'Sustainable Biomedical Engineering', 'Sustainable Environmental Engineering', 'Sustainable Engineering Physics', 'Sustainable Aerospace Engineering', 'Sustainable Materials Engineering', 'Sustainable Mining Engineering', 'Sustainable Oil and Gas Engineering', 'Sustainable Energy Engineering', 'Sustainable Systems Engineering', 'Sustainable Development Engineering', 'Sustainable Infrastructure Engineering', 'Sustainable Resources Engineering', 'Sustainable Environmental Engineering', 'Sustainable Chemical Engineering', 'Sustainable Petroleum Engineering', 'Sustainable Geological Engineering', 'Sustainable Geomatics Engineering', 'Sustainable Biomedical Engineering', 'Sustainable Environmental Engineering', 'Sustainable Engineering Physics', 'Sustainable Aerospace Engineering', 'Sustainable Materials Engineering', 'Sustainable Mining Engineering', 'Sustainable Oil and Gas Engineering', 'Sustainable Energy Engineering', 'Sustainable Systems Engineering', 'Sustainable Development Engineering', 'Sustainable Infrastructure Engineering', 'Sustainable Resources Engineering', 'Sustainable Environmental Engineering', 'Sustainable Chemical Engineering', 'Sustainable Petroleum Engineering', 'Sustainable Geological Engineering', 'Sustainable Geomatics Engineering', 'Sustainable Biomedical Engineering', 'Sustainable Environmental Engineering', 'Sustainable Engineering Physics', 'Sustainable Aerospace Engineering', 'Sustainable Materials Engineering', 'Sustainable Mining Engineering', 'Sustainable Oil and Gas Engineering', 'Sustainable Energy Engineering', 'Sustainable Systems Engineering', 'Sustainable Development Engineering', 'Sustainable Infrastructure Engineering', 'Sustainable Resources Engineering', 'Sustainable Environmental Engineering', 'Sustainable Chemical Engineering', 'Sustainable Petroleum Engineering', 'Sustainable Geological Engineering', 'Sustainable Geomatics Engineering', 'Sustainable Biomedical Engineering', 'Sustainable Environmental Engineering', 'Sustainable Engineering Physics', 'Sustainable Aerospace Engineering', 'Sustainable Materials Engineering'],
                courseInputValue: '',
                selectedEq: '',
                eqTypes: ['=', '>', '<', '>=', '<='],
                isOnline: false,
            }
        },
        methods: {

            toggleMode() {
                this.isOnline = !this.isOnline;
                // You can emit an event here if you want to notify the parent component about the mode change
                // this.$emit('mode-changed', this.isOnline);
            },
            closeAdvancedSearch(){
                this.$emit('close')
            },
            appluAdvancedSearch(){
                this.$emit('applyadvancedsearch')
            }
        }
    }
</script>
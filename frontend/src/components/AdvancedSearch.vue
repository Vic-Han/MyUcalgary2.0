<template>
    <div class="fixed w-screen h-screen z-30 opacity-50 bg-black-100"></div>
    <div class="fixed w-fit h-96 z-40 bg-white-100 rounded-xl left-1/2 -translate-x-1/2 top-1/3 -translate-y-1/2">
        <div @click="closeAdvancedSearch" class="absolute p-2 right-0">
            <svg xmlns="http://www.w3.org/2000/svg" class=" h-10 w-10 fill-grey-200 cursor-pointer hover:fill-red-100" viewBox="0 -960 960 960">
                <path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/>
            </svg>
        </div>
        <form class="bg-white-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">

        <!-- Major -->
        <div class="mb-4 flex items-center justify-between pt-6">
            <label class="block text-grey-200 font-semibold text-xl mb-2 mr-2" for="requirement-type">
                Major
            </label>
            <div class="relative">
            <select v-model="selectedMajorType" class="relative w-28 rounded-lg border-2 border-grey-200 outline-blue-500 focus:border-blue-500 py-2 px-4 m-3 text-center">
                <option v-for="type in majorType" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedFacultyType }" class="text-left">{{ type }}</option>
            </select>
            </div>
        </div>

        <!-- Course Number -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-grey-200 font-semibold text-xl mb-2 mr-2" for="requirement-type">
                Course Number
            </label>
            <div class="flex">
            <select v-model="selectedEq" class="relative w-20 rounded-lg border-2 outline-blue-500 border-grey-200 focus:border-blue-500 py-2 px-1 my-3 text-center">
                <option v-for="type in eqTypes" :key="type" :value="type" :class="{ 'bg-red-100': type === selectedFacultyType }" class="">{{ type }}</option>
            </select>
            <input type="text" id="inputBox" v-model="courseInputValue" class="w-24 rounded-lg border-2 border-grey-200 outline-blue-500 focus:border-blue-500 py-2 px-2 m-3">
            </div>
        </div>

        <!-- Mode -->
        <div class="mb-4 flex items-center justify-between">
            <label class="block text-grey-200 font-semibold text-xl mb-2 mr-2" for="mode">
            Mode
            </label>
            <div class="">
                <div class="bg-white-100  rounded-lg h-fit w-48 py-1 px-1 my-3  cursor-pointer border-2 border-grey-200"
                    @click="toggleMode">
                    <div class=" rounded-md h-8 w-1/2 left-1 shadow-md transition-transform duration-150 ease-in-out border-2" :class="{ 'translate-x-full bg-white-100 border-grey-200': !isOnline, 'bg-red-100 border-red-100': isOnline }">
                        <span class="text-sm" :class="{ 'text-grey-200': !isOnline, 'text-white-100': isOnline }">
                            {{ isOnline ? 'Online' : 'Offline' }}
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex items-center">
            <label class="block text-grey-200 font-semibold text-xl mb-2 mr-2">Time</label>
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
        <div class="mb-4 pt-4">
          <label class="block text-grey-200 font-semibold text-xl mb-2 mr-2 text-left" for="requirement-type">
            Days
          </label>
          <div class="flex space-x-2">
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" :class="{'bg-red-100 border-red-100 text-white-100': days[0] }" @click="days[0] = !days[0]">Monday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" :class="{'bg-red-100 border-red-100 text-white-100': days[1] }" @click="days[1] = !days[1]">Tuesday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" :class="{'bg-red-100 border-red-100 text-white-100': days[2] }" @click="days[2] = !days[2]">Wednesday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" :class="{'bg-red-100 border-red-100 text-white-100': days[3] }" @click="days[3] = !days[3]">Thursday</button>
            <button type="button" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded shadow" :class="{'bg-red-100 border-red-100 text-white-100': days[4] }" @click="days[4] = !days[4]">Friday</button>
          </div>
        </div>
  
        <!-- Search button -->
        <div class="flex items-center justify-center">
          <button class="bg-white-100 border-2 border-grey-200 hover:bg-red-100 hover:text-white-100 hover:border-red-100 font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
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
                days: [
                    false,
                    false,
                    false,
                    false,
                    false                    
                ],
                selectedMajorType: '',
                majorType: ['MATH', 'SENG', 'ENSF', 'ENEL', 'ECON', 'ENGG', 'INTE', 'CPSC', 'PHIL', 'BMEN', 'ENCI', 'ENCM', 'ENME', 'GRST', 'SOCI', 'DNCE'],
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
            applyAdvancedSearch(){
                this.$emit('applyadvancedsearch')
            },
        }
    }
</script>
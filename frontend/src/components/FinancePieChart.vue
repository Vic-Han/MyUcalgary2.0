<template>
        <div class="flex flex-row pt-6 px-6">
            <div class="w-2/3 text-left font-semibold text-3xl">Finances</div>
            <div class="flex flex-row" v-if="status == 'Paid'">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-green-100" viewBox="0 -960 960 960">
                    <path d="m344-60-76-128-144-32 14-148-98-112 98-112-14-148 144-32 76-128 136 58 136-58 76 128 144 32-14 148 98 112-98 112 14 148-144 32-76 128-136-58-136 58Zm94-278 226-226-56-58-170 170-86-84-56 56 142 142Z"/>
                </svg>
                <div class="flex items-center pl-2 italic text-lg text-green-100">{{ status }}</div>
            </div>
            <div class="flex flex-row" v-if="status == 'Pending'">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-yellow-100" viewBox="0 -960 960 960">
                    <path d="m612-292 56-56-148-148v-184h-80v216l172 172ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-400Zm0 320q133 0 226.5-93.5T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 133 93.5 226.5T480-160Z"/>
                </svg>
                <div class="flex items-center pl-2 italic text-lg text-yellow-100">{{ status }}</div>
            </div>
            <div class="flex flex-row" v-if="status == 'Overdue'">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-red-100" viewBox="0 -960 960 960">
                    <path d="m40-120 440-760 440 760H40Zm138-80h604L480-720 178-200Zm302-40q17 0 28.5-11.5T520-280q0-17-11.5-28.5T480-320q-17 0-28.5 11.5T440-280q0 17 11.5 28.5T480-240Zm-40-120h80v-200h-80v200Zm40-100Z"/>
                </svg>
                <div class="flex items-center pl-2 italic text-lg text-red-100">{{ status }}</div>
            </div>
        </div>
        <div class="pt-8 text-grey-200 text-lg">{{ term }} Fees</div>
        <div v-if="status == 'Overdue'" class="my-5 py-4 px-6 w-fit relative left-1/2 -translate-x-1/2 border-4 rounded-lg border-red-100 font-semibold text-3xl text-red-100">${{ amount }}</div>
        <div v-if="status == 'Pending'" class="my-5 py-4 px-6 w-fit relative left-1/2 -translate-x-1/2 border-4 rounded-lg border-yellow-100 font-semibold text-3xl text-yellow-100">${{ amount }}</div>
        <div v-if="status == 'Paid'" class="my-5 py-4 px-6 w-fit relative left-1/2 -translate-x-1/2 border-4 rounded-lg border-green-100 font-semibold text-3xl text-green-100">${{ amount }}</div>
        <div class="text-grey-200 text-lg">Due by: {{ due }}</div>
</template>

<script>
    export default{
        name : 'FinancePieChart',
        props:{
            term: {
                type: String,
                required: true
            },
            amount: {
                type: String,
                required: true
            },
            status: {
                type: String,
                required: true
            },
            due: {
                type: String,
                required: true
            }
        }
    }
</script>
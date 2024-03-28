<template>
  <div class="bg-grey-100 flex flex-col p-5 w-full">
      <div class="flex flex-row gap-x-4">
          <div class="flex flex-col gap-y-4"> 
              <div class="bg-white-100 p-10 rounded-xl shadow-lg"> 
                 <div class="font-semibold text-3xl mb-4"> {{ currentTerm }} </div>
                 <div class="rounded-full w-64 h-64 mx-8 border-grey-200 border-2" :style="pieChartStyle"></div>
                 <div class="flex flex-row mt-8 justify-center">
                        <div class="flex items-center mx-4">
                          <span class="inline-block w-4 h-4 bg-red-100 mr-1 rounded-sm"></span><span class="text-grey-200">Due</span>
                        </div>
                        <div class="flex items-center mx-2">
                          <span class="inline-block w-4 h-4 bg-green-100 mr-1 rounded-sm"></span><span class="text-grey-200">Paid</span>
                        </div>
                        <div class="flex items-center mx-4">
                          <span class="inline-block w-4 h-4 bg-yellow-100 mr-1 rounded-sm"></span><span class="text-grey-200">Awards</span>
                        </div>
                 </div>
              </div>
              <div class="bg-white-100  flex flex-col p-5 rounded-xl shadow-lg h-96">
                <FinancePieChart :term="FinancePreview.term" :amount="FinancePreview.amount" :status="FinancePreview.status" :due="FinancePreview.due"/>
              </div>
          </div>
          <div class="bg-white-100 px-5 pt-5 pb-7 rounded-xl shadow-lg"> 
            <div class="relative flex justify-end mr-4 mb-8">
                <select v-model="selectedTerm"
                    class="rounded-lg border-2 focus:outline-none 
                    focus:ring-2 focus:ring-gray-600 focus:border-red transition duration-200 ease-in-out appearance-none bg-white py-2 pr-10 pl-2 text-left">
                    <option v-for="(value,key) in terms" :value="key" :key="key" class="mb-2">
                        {{ key }}
                    </option>
                </select>
                <svg class="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 pointer-events-none text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </div>
                <div class="grid grid-cols-5">
                  <div class=" text-center rounded-tl-xl px-4 py-4 bg-gray-300 border border-gray-300 cursor-pointer" v-bind:class="{'bg-white-100 border-b-0' : activeTab =='all'}" @click="activeTab = 'all' ">All</div>
                  <div class=" text-center px-4 py-4 bg-gray-300 border border-gray-300 cursor-pointer" v-bind:class="{'bg-white-100 border-b-0' : activeTab =='fee'}" @click="activeTab = 'fee' ">Fees</div>
                  <div class=" text-center px-4 py-4 bg-gray-300 border border-gray-300 cursor-pointer" v-bind:class="{'bg-white-100 border-b-0' : activeTab =='payment'}" @click="activeTab = 'payment'">Payments</div>
                  <div class=" text-center px-4 py-4 bg-gray-300 border border-gray-300 cursor-pointer" v-bind:class="{'bg-white-100 border-b-0' : activeTab =='scholarship'}" @click=" activeTab = 'scholarship'">Scholarships</div>
                  <div class=" text-center rounded-tr-xl px-4 pt-4 pb-4 bg-gray-300 border border-gray-300 cursor-pointer" v-bind:class="{'bg-white-100 border-b-0' : activeTab =='award'}" @click="activeTab = 'award'">Awards</div>
                </div>
                <div class="flex flex-col rounded-lg shadow-md border-b border-r border-l border-gray-300 rounded-tl-none">
                  <div class="flex flex-row">
                      <div class="p-4 text-left w-60"> Item </div>
                      <div class="p-4 text-left w-36"> Type </div>
                      <div class="p-4 text-left w-36"> Posted Date </div>
                      <div class="p-4 text-left w-36"> Charge </div>
                      <div class="p-4 text-left w-36"> Payment </div>
                      <div class="p-4 text-left w-36"> Refund </div>
                  </div>
                  <div v-for='(item, index) in terms[selectedTerm]' :key="index">
                      <div v-if="item.type == activeTab || activeTab == 'all'" class="flex flex-row border-t-2 border-gray-200">
                          <div class="p-4 text-left w-60"> {{ item.name }} </div>
                          <div class="p-4 text-left w-36"> {{ item.type }} </div>
                          <div class="p-4 text-left w-36"> {{ item.date }} </div>
                          <div class="p-4 text-left w-36"> {{ paymentType(item.type) == 'charge' ? item.amount : 0}} </div>
                          <div class="p-4 text-left w-36"> {{ paymentType(item.type) == 'payment' ? item.amount  : 0 }} </div>
                          <div class="p-4 text-left w-36"> {{ paymentType(item.type) == 'refund' ? item.amount  : 0 }} </div>
                      </div>
                  </div>
                </div>
          </div>
      </div>
  </div>
</template>

<script>
import FinancePieChart from '../components/FinancePieChart'
export default {
  name: 'FinanceBreakdown',
  emits: ['show-navbar', 'toggle-selected'],
  components: {
    FinancePieChart
  },
  data() {
    return {
      selectedTerm: 'Winter 2024',
      currentTerm: 'Winter 2024',
      activeTab: 'all',
      terms: {},
      pieChartColors: {
        due: '#D6001C',
        paid: '#47A67C',
        awards: '#FFCD00',
      },
      pieChartSegments: {
        due: { start: '0%', end: '60%' },
        paid: { start: '60%', end: '80%' },
        awards: { start: '80%', end: '100%' },
      },
      FinancePreview: {
        term: "Winter 2024",
        amount: "3,125.03",
        status: "Paid",
        due: "February 25, 2024"
      }
    };
  },
  methods: {
    fetchFinancialData() {
    const serverPath = this.$store.state.serverPath;
    const apiPath = "/api/student-finances/";
    const previewApiPath = '/api/dashboard/';
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': `Token ${this.$cookies.get("auth-token")}`
    };

    fetch(`${serverPath}${apiPath}`, { headers })
      .then(response => response.json())
      .then(data => {
        // console.log('API data:', data); 
        this.terms = data.activity;
        this.paid = data.paid;
        this.awards = data.awards;
        this.due = data.due;
        
        const total = this.paid + this.awards + this.due;
        if(total == 0){
          this.pieChartSegments = {
            paid: { start: '0%', end: '100%' },
          }
        }
        else{
          this.pieChartSegments = {
            due: { start: '0%', end: `${(this.due / total) * 100}%` },
            paid: { start: `${(this.due / total) * 100}%`, end: `${((this.due + this.paid) / total) * 100}%` },
            awards: { start: `${((this.due + this.paid) / total) * 100}%`, end: '100%' },
          }
        }
      })
      .catch(error => console.error('Error fetching data:', error));

      fetch(`${serverPath}${previewApiPath}`, { headers })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        for(const [key,value] of Object.entries(data.finances)){
          this.selectedTerm = key;
          this.currentTerm = key;
          this.FinancePreview.term = key
          this.FinancePreview.amount = value.net_balance >= 0 ? value.credits : value.debits + value.credits
          this.FinancePreview.status = value.net_balance < 0 ? "Unpaid" : "Paid"
          this.FinancePreview.due = value.due
        }
      }).catch(error => console.error('Error fetching data:', error));
    },

    paymentType(type){
      if(type === 'scholarship'){
          return 'payment'
      }
      if(type === 'award'){
          return 'payment'
      }
      if (type === 'payment'){
          return 'payment'
      }
      if(type === 'fee'){
          return 'charge'
      }
      else{
          return 'refund'
      }
    }
  },
  computed: {
    pieChartStyle() {
      let gradient = 'conic-gradient(';
      for (const [key, segment] of Object.entries(this.pieChartSegments)) {
        const color = this.pieChartColors[key];
        gradient += `${color} ${segment.start}, ${color} ${segment.end}, `;
      }
      gradient = gradient.slice(0, -2) + ')';
      return { background: gradient };
    }
  },
  created(){
    
    this.$emit('show-navbar')
    this.$emit('toggle-selected', 'finances');
    this.fetchFinancialData();
  }
};

</script>

<style>

</style>
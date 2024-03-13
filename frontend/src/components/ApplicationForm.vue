<template>
  <div class="bg-white-100 p-8">
    <!-- Top Navigation -->
    <div class="flex justify-between items-center mb-6">
      <a href="#" class="text-black text-xl font-bold editable-text" @click.prevent="goToPreviousStep">← Application
        Form</a>
    </div>

    <!-- Centered Progress Indicator Container -->
    <!-- Further increased bottom margin (mb-12 to mb-16) for additional space -->
    <!-- Centered Progress Indicator Container -->
    <!-- Centered Progress Indicator Container -->
    <div class="flex justify-center items-center mb-16 ">
      <div class="flex items-center justify-between w-full max-w-4xl px-4 mt-8">
        <!-- Progress Steps -->
        <div class="flex flex-col items-center">
          <!-- Dynamic class binding for step 1 -->
          <div :class="{ 'bg-green-400': currentStep > 1, 'bg-gray-200': currentStep === 1 }"
            class="w-16 h-16 rounded-full flex items-center justify-center text-white font-bold">
            1
          </div>
          <div class="text-sm text-gray-500 mt-2 flex flex-col items-center w-16">
            <span>Program</span>
            <span>Selection</span>
          </div>
        </div>
        <!-- Progress bar line -->
        <!-- Adjust margin top to half of circle height to align with the middle -->
        <div class="flex-auto border-t-2 border-gray-200 -translate-y-4"></div>
        <div class="flex flex-col items-center">
          <div :class="{ 'bg-green-400': currentStep >= 3, 'bg-gray-200': currentStep < 3 }"
            class="w-16 h-16 rounded-full flex items-center justify-center text-gray-500 font-bold">
            2
          </div>
          <div class="text-sm text-gray-500 mt-2 flex flex-col items-center w-16">
            <span>Personal</span>
            <span>Info</span>
          </div>
        </div>
        <!-- Progress bar line -->
        <div class="flex-auto border-t-2 border-gray-200 -translate-y-4"></div>

        <div class="flex flex-col items-center">
          <div :class="{ 'bg-green-400': currentStep >= 4, 'bg-gray-200': currentStep < 4 }"
            class="w-16 h-16 rounded-full flex items-center justify-center text-gray-500 font-bold">
            3
          </div>
          <div class="text-sm text-gray-500 mt-2 flex flex-col items-center w-16">
            <span>Application</span>
            <span>Documents</span>
          </div>
        </div>
        <!-- Progress bar line -->
        <div class="flex-auto border-t-2 border-gray-200 -translate-y-4"></div>

        <div class="flex flex-col items-center">
          <div class="w-16 h-16 bg-gray-200 rounded-full flex items-center justify-center text-gray-500 font-bold">4
          </div>
          <div class="text-sm text-gray-500 mt-2 flex flex-col items-center">
            <span>Review &</span>
            <span>Submit</span>
          </div>
        </div>
      </div>
    </div>


    <div v-if="currentStep === 1">
      <!-- Form Layout -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 ml-24">
        <!-- Dropdowns Section -->
        <div>
          <!-- Further increased top margin (from mt-8 to mt-12) for each dropdown for additional space -->
          <!-- Faculty Dropdown -->
          <div class="mt-12">
            <label for="faculty" class="block text-lg font-bold text-black mb-1 text-left">Faculty</label>
            <select id="faculty" name="faculty"
              class="mt-1 block w-full h-10 px-2 py-2 border-2 border-gray-300 text-black rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              v-model="personalInfo.faculty"> <!-- Added v-model -->
              <option value="science">Science</option>
              <option value="engineering">Engineering</option>
              <option value="arts">Arts</option>
              <option value="business">Business</option>
            </select>

          </div>

          <!-- Program Dropdown -->
          <div class="mt-12">
            <label for="program" class="block text-lg font-bold text-black mb-1 text-left">Program</label>
            <select id="program" name="program"
              class="mt-1 block w-full h-10 px-2 py-2 border-2 border-gray-300 text-black rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              v-model="personalInfo.program">
              <option value="computer-science">Computer Science</option>
              <option value="mechanical-engineering">Mechanical Engineering</option>
              <option value="fine-arts">Fine Arts</option>
              <option value="marketing">Marketing</option>
            </select>
          </div>


          <!-- Sponsor Dropdown -->
          <div class="mt-12">
            <label for="sponsor" class="block text-lg font-bold text-black mb-1 text-left">Sponsor</label>
            <select id="sponsor" name="sponsor"
              class="mt-1 block w-full h-10 px-2 py-2 border-2 border-gray-300 text-black rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              v-model="personalInfo.sponsor">
              <option value="self">Self</option>
              <option value="government">Government Scholarship</option>
              <option value="private">Private Sponsorship</option>
            </select>
          </div>






        </div>
        <div class="info-section md:col-span-3 ml-64">
          <!-- Cost Info -->
          <div class="cost-info flex flex-col space-y-2 mt-12 text-left">
            <div class="text-base font-medium text-gray-700 font-semibold">Estimate Cost:</div>
            <div class="text-base font-semibold">$12,300</div>
          </div>

          <!-- Start Date & Length Info -->
          <div class="start-date-info flex flex-col space-y-2 mt-12 text-left">
            <div class="text-base font-medium text-gray-700 font-semibold">Program start Date & Length:</div>
            <div class="text-base font-semibold">Fall 2024<br>4 Year</div>
          </div>
        </div>





      </div>

    </div>

    <div v-if="currentStep === 2" class="mt-8 max-w-4xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 -ml-12">
        <!-- UCID Field -->
        <div class="mb-4">
          <label for="ucid" class="block text-lg font-bold text-black mb-1 text-left">UCID</label>
          <input type="text" id="ucid" name="ucid" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.ucid">
        </div>

        <!-- First Name Field -->
        <div class="mb-4">
          <label for="first-name" class="block text-lg font-bold text-black mb-1 text-left">First Name</label>
          <input type="text" id="first-name" name="first-name" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.firstName">
        </div>

        <!-- Last Name Field -->
        <div class="mb-4">
          <label for="last-name" class="block text-lg font-bold text-black mb-1 text-left">Last Name</label>
          <input type="text" id="last-name" name="last-name" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.lastName">
        </div>

        <!-- UC Email Field -->
        <div class="mb-4">
          <label for="uc-email" class="block text-lg font-bold text-black mb-1 text-left">UC Email</label>
          <input type="email" id="uc-email" name="uc-email" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.ucEmail">
        </div>

        <!-- Cell / Phone Numbers Field -->
        <div class="mb-4">
          <label for="cell-phone" class="block text-lg font-bold text-black mb-1 text-left">Cell / Phone Numbers</label>
          <input type="tel" id="cell-phone" name="cell-phone" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.phone">
        </div>

        <!-- Home Address Field -->
        <div class="mb-4">
          <label for="home-address" class="block text-lg font-bold text-black mb-1 text-left">Home Address</label>
          <input type="text" id="home-address" name="home-address" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.address">
        </div>

        <!-- Home Address 2 Field -->
        <div class="mb-4">
          <label for="home-address-2" class="block text-lg font-bold text-black mb-1 text-left">Home Address 2</label>
          <input type="text" id="home-address-2" name="home-address-2" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.address2">
        </div>

        <!-- Country Dropdown -->
        <div class="mb-4">
          <label for="country" class="block text-lg font-bold text-black mb-1 text-left">Country*</label>
          <select id="country" name="country" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.country">
            <option value="usa">USA</option>
            <option value="canada">Canada</option>
            <option value="uk">UK</option>
            <option value="australia">Australia</option>
          </select>
        </div>



        <!-- Province Dropdown -->
        <div class="mb-4">
          <label for="province" class="block text-lg font-bold text-black mb-1 text-left">Province</label>
          <select id="province" name="province" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.province">
            <option value="alberta">Alberta</option>
            <option value="british-columbia">British Columbia</option>
            <option value="manitoba">Manitoba</option>
            <option value="new-brunswick">New Brunswick</option>
            <option value="newfoundland-and-labrador">Newfoundland and Labrador</option>
          </select>
        </div>



        <!-- City Field -->
        <div class="mb-4">
          <label for="city" class="block text-lg font-bold text-black mb-1 text-left">City*</label>
          <input type="text" id="city" name="city" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.city">
        </div>

        <!-- Postal Code Field, assuming it should also follow the three-column layout -->
        <div class="mb-4">
          <label for="postal-code" class="block text-lg font-bold text-black mb-1 text-left">Postal Code*</label>
          <input type="text" id="postal-code" name="postal-code" class="w-full h-10 border-2 border-gray-300 px-2"
            v-model="personalInfo.postalCode">
        </div>


      </div>
    </div>


    <!-- Step 4: Review & Submit -->
    <div v-if="currentStep === 4" class="mt-4 max-w-4xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 -ml-16">
        <!-- Replace the content here with your Review & Submit information -->
        <!-- Each field now displays the entered information instead of input fields -->
        <div class="mb-4">
          <label class="block text-lg font-bold text-black mb-1 text-left">Faculty</label>
          <div class="w-full h-10 px-2 py-2 border-2 border-gray-300">{{ personalInfo.faculty }}</div>
        </div>
        <div class="mb-4">
          <label class="block text-lg font-bold text-black mb-1 text-left">Program</label>
          <div class="w-full h-10 px-2 py-2 border-2 border-gray-300">{{ personalInfo.program }}</div>
        </div>
        <div class="mb-4">
          <label class="block text-lg font-bold text-black mb-1 text-left">Sponsor</label>
          <div class="w-full h-10 px-2 py-2 border-2 border-gray-300">{{ personalInfo.sponsor }}</div>
        </div>
        <div class="mb-4">
          <label for="ucid" class="block text-lg font-bold text-black mb-1 text-left">UCID</label>
          <input type="text" id="ucid" class="w-full h-10 border-2 border-gray-300 px-2" :value="personalInfo.ucid"
            readonly>
        </div>

        <div class="mb-4">
          <label for="first-name" class="block text-lg font-bold text-black mb-1 text-left">First Name</label>
          <input type="text" id="first-name" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.firstName" readonly>
        </div>

        <div class="mb-4">
          <label for="last-name" class="block text-lg font-bold text-black mb-1 text-left">Last Name</label>
          <input type="text" id="last-name" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.lastName" readonly>
        </div>

        <div class="mb-4">
          <label for="uc-email" class="block text-lg font-bold text-black mb-1 text-left">UC Email</label>
          <input type="email" id="uc-email" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.ucEmail" readonly>
        </div>

        <div class="mb-4">
          <label for="cell-phone" class="block text-lg font-bold text-black mb-1 text-left">Cell / Phone Numbers</label>
          <input type="tel" id="cell-phone" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.phone" readonly>
        </div>

        <div class="mb-4">
          <label for="home-address" class="block text-lg font-bold text-black mb-1 text-left">Home Address</label>
          <input type="text" id="home-address" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.address" readonly>
        </div>

        <div class="mb-4">
          <label for="home-address-2" class="block text-lg font-bold text-black mb-1 text-left">Home Address 2</label>
          <input type="text" id="home-address-2" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.address2" readonly>
        </div>

        <div class="mb-4">
          <label for="country" class="block text-lg font-bold text-black mb-1 text-left">Country</label>
          <select id="country" class="w-full h-10 border-2 border-gray-300 px-2" :value="personalInfo.country" disabled>
            <!-- Options go here -->
          </select>
        </div>

        <div class="mb-4">
          <label for="province" class="block text-lg font-bold text-black mb-1 text-left">Province</label>
          <select id="province" class="w-full h-10 border-2 border-gray-300 px-2" :value="personalInfo.province"
            disabled>
            <!-- Options go here -->
          </select>
        </div>

        <div class="mb-4">
          <label for="city" class="block text-lg font-bold text-black mb-1 text-left">City</label>
          <input type="text" id="city" class="w-full h-10 border-2 border-gray-300 px-2" :value="personalInfo.city"
            readonly>
        </div>

        <div class="mb-4">
          <label for="postal-code" class="block text-lg font-bold text-black mb-1 text-left">Postal Code</label>
          <input type="text" id="postal-code" class="w-full h-10 border-2 border-gray-300 px-2"
            :value="personalInfo.postalCode" readonly>
        </div>

      </div>
      <!-- Shared Continue Button - Specific to Step 4 -->
      <!-- Shared Continue Button -->
      <!-- <div class="flex justify-end mt-4" :class="{ 'mb-4': currentStep !== 4, '-mb-32': currentStep === 4 }">
        <button class="bg-white hover:bg-red-700 text-red-500 font-bold py-2 px-4 rounded-md transition-colors"
          @click="goToNextStep">
          Continue
        </button>
      </div> -->


    </div>
    <!-- Shared Continue Button -->
    <div class="flex justify-end mt-4" :class="{ 'mb-4': currentStep === 4 }">
      <button class="bg-white hover:bg-white-700 text-red-500 border border-red-500 font-bold py-2 px-4 rounded-md"
        @click="goToNextStep">
        {{ currentStep === 4 ? 'Submit' : 'Continue' }}
      </button>
    </div>




  </div>
</template>




<script>
export default {
  name: 'ApplicationForm',
  data() {
    return {
      currentStep: 1,
      personalInfo: {
        ucid: '',
        firstName: '',
        lastName: '',
        ucEmail: '',
        phone: '',
        address: '',
        address2: '', // Ensure you have this if you're capturing a second address line
        country: '',
        province: '', // Make sure to include province if you're capturing it
        city: '',
        postalCode: '',
        faculty: '', // Added
        program: '', // Added
        sponsor: '' // Added
      }
    };
  },

  methods: {
    goToNextStep() {
      if (this.currentStep < 4) {
        this.currentStep++;
      }
      else{
        // call back end
        this.$emit('submit')
      }
    },
    goToPreviousStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
      }
      else{
        this.$emit('cancel')
      }
    },
  },


}
</script>

<style>
/* Tailwind CSS is already applied */
/* Additional style for the fourth step */
.mb-4 {
  margin-bottom: -10rem;
  /* Adjust this value to ensure the button is visible */
}
</style>
import { mount } from '@vue/test-utils';
import ApplicationForm from '@/components/ApplicationForm.vue';

describe('ApplicationForm.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(ApplicationForm);
  });

  it('initializes with the correct element visibility and first step active', () => {
    expect(wrapper.find('.editable-text').text()).toContain('Application Form');
    expect(wrapper.find('.bg-green-400').exists()).toBe(false); // No steps completed
    expect(wrapper.vm.currentStep).toBe(1); // First step is active
  });


  it('displays the form fields for the current step only', async () => {
    expect(wrapper.findAll('input').length).toBe(0); // No input fields in the first step
    await wrapper.setData({ currentStep: 2 });
    expect(wrapper.findAll('input').length).toBeGreaterThan(0); // Input fields for step 2 are shown
  });

  it('changes the button text on the final step', async () => {
    expect(wrapper.find('button').text()).toContain('Continue');
    await wrapper.setData({ currentStep: 4 });
    expect(wrapper.find('button').text()).toContain('Submit');
  });

  it('emits submit event when submit button is clicked on the final step', async () => {
    await wrapper.setData({ currentStep: 4 });
    await wrapper.find('button').trigger('click');
    expect(wrapper.emitted()).toHaveProperty('submit');
  });

  it('navigates to the previous step correctly', async () => {
    await wrapper.setData({ currentStep: 3 });
    await wrapper.vm.goToPreviousStep();
    expect(wrapper.vm.currentStep).toBe(2);
  });

  it('shows the correct label and options for the Faculty dropdown in step 1', () => {
    const facultySelect = wrapper.find('#faculty');
    expect(facultySelect.exists()).toBe(true);
    expect(facultySelect.find('option[value="science"]').exists()).toBe(true); // Checks for one of the options
  });

});

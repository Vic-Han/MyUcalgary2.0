import { mount } from '@vue/test-utils';
import AcademicSchedulePopup from '@/components/AcademicSchedulePopup.vue'; 

describe('AcademicSchedulePopup.vue', () => {
  it('should mount the component', () => {
    const wrapper = mount(AcademicSchedulePopup, {
      props: {
        requirements: {} 
      }
    });
    expect(wrapper.isVisible()).toBe(true);
  });

  it('emits close event when close button is clicked', async () => {
    const wrapper = mount(AcademicSchedulePopup, {
      props: {
        requirements: {} 
      }
    });
    await wrapper.find('button').trigger('click'); 
    expect(wrapper.emitted()).toHaveProperty('close');
  });

  it('displays the correct title', () => {
    const wrapper = mount(AcademicSchedulePopup, {
      props: {
        requirements: {} 
      }
    });
    expect(wrapper.find('h2').text()).toContain('Degree Requirements');
  });

  it('displays colors for course statuses correctly', () => {
    const wrapper = mount(AcademicSchedulePopup, {
      props: {
        requirements: {} 
      }
    });

    const openStatusColor = wrapper.find('.bg-green-500');
    const waitlistStatusColor = wrapper.find('.bg-yellow-500');
    const closedStatusColor = wrapper.find('.bg-red-500');

    expect(openStatusColor.exists()).toBe(true);
    expect(waitlistStatusColor.exists()).toBe(true);
    expect(closedStatusColor.exists()).toBe(true);
  });
  
  

});

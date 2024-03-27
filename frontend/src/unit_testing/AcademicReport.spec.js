import { shallowMount } from '@vue/test-utils';
import AcademicReport from '@/views/AcademicReport.vue';

describe('AcademicReport.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(AcademicReport, {
      propsData: {

      }
    });
  });

  it('renders program information section', () => {
    const programInformation = wrapper.find('.program-information');
    expect(programInformation.exists()).toBe(true);
    expect(programInformation.text()).toContain('Program Information');
  });

  it('displays degree progress section', () => {
    expect(wrapper.text()).toContain('Degree Progress');
    const progress = wrapper.find('.bg-green-100');
    expect(progress.exists()).toBe(true);
  });

  it('displays correct progress percentage', async () => {
    await wrapper.setData({ completedProgress: 75 });
    const progressText = wrapper.find('.bg-green-100').text();
    expect(progressText).toContain('75%');
  });

  it('renders course breakdown section', () => {
    expect(wrapper.text()).toContain('Course Breakdown');
    const courseBreakdown = wrapper.find('.h-144');
    expect(courseBreakdown.exists()).toBe(true);
  });

  it('toggles course details on click', async () => {
    await wrapper.setData({ 
      requiredCourses: [
        {
          description: "Test Course",
          expanded: false
        }
      ]
    });

    const toggleIcon = wrapper.find('svg'); 
    await toggleIcon.trigger('click');

    expect(wrapper.vm.requiredCourses[0].expanded).toBe(true);
  });


});

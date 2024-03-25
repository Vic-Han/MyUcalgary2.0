import { mount } from '@vue/test-utils';
import GradePreview from '@/components/GradePreview.vue';

describe('GradePreview.vue', () => {
  const propsData = {
    average: 3.5,
    letter: 'A',
    courses: [
      { name: 'Math 101', letter: 'A' },
      { name: 'English 101', letter: 'B' }
    ],
    term: 'Fall 2024',
    year: 2,
    unitsEnrolled: 10,
    plan: 'Computer Science',
    program: 'BSc',
    dashboardView: false
  };

  let wrapper;
  beforeEach(() => {
    wrapper = mount(GradePreview, { propsData });
  });

  it('renders term title', () => {
    expect(wrapper.find('.text-2xl').text()).toContain(propsData.term);
  });

  it('displays average GPA correctly', () => {
    expect(wrapper.find('.rounded-full').text()).toContain(propsData.average.toString());
  });

  it('applies correct color based on letter grade', () => {
    const circleDiv = wrapper.find('.rounded-full');
    expect(circleDiv.classes()).toContain('bg-grade-A-background'); 
  });

  it('renders correct number of courses', () => {
    expect(wrapper.findAll('div.mx-3.text-lg').length).toBe(propsData.courses.length);
  });

  it('displays additional information when not in dashboard view', () => {
    expect(wrapper.find('div.text-left.text-sm').exists()).toBe(true);
    expect(wrapper.text()).toContain(`Level: ${propsData.year}`);
    expect(wrapper.text()).toContain(`Units Enrolled: ${propsData.unitsEnrolled}`);
  });

  it('applies correct bar width and color based on course letter grade', () => {
    const firstCourseBar = wrapper.find('div.h-8').classes();
    expect(firstCourseBar).toContain('bg-grade-A'); 
    expect(firstCourseBar).toContain('w-96'); 
  });

  it('conditionally hides detailed info in dashboard view', async () => {
    await wrapper.setProps({ dashboardView: true });
    expect(wrapper.find('div.text-left.text-sm').exists()).toBe(false);
  });
});

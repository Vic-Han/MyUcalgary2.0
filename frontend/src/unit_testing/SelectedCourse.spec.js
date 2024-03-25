import { mount } from '@vue/test-utils';
import SelectedCourse from '@/components/SelectedCourse.vue';

describe('SelectedCourse.vue', () => {
  const courseData = {
    name: 'COMP SCI',
    title: 'Introduction to Computer Science',
    included: 'sched',
    lectures: [{
      name: 'Lec 01',
      start: 9,
      end: 10.5,
      days: ['M', 'W', 'F'],
      roomno: 'EN 204',
      Prof: 'Dr. Smith'
    }],
    tutorials: [{
      name: 'Tut 01',
      start: 11,
      end: 12.5,
      days: ['T', 'R'],
      roomno: 'EN 205',
    }],
    combinations: [['Lec 01', 'Tut 01']],
    selected: 0,
    selectedIndices: [true]
  };

  const wrapper = mount(SelectedCourse, {
    props: { 
      course: courseData,
      number: 1
    }
  });

  it('displays the course name and title', () => {
    expect(wrapper.text()).toContain(courseData.name);
    expect(wrapper.text()).toContain(courseData.title);
  });

  it('applies course color based on the course number', () => {
    expect(wrapper.vm.courseColor()).toContain('bg-course-200');
  });

  it('shows lecture and tutorial information correctly', () => {
    const lectureInfo = courseData.lectures[0];
    const tutorialInfo = courseData.tutorials[0];
    expect(wrapper.text()).toContain(`${lectureInfo.name}`);
    expect(wrapper.text()).toContain(`${tutorialInfo.name}`);
    expect(wrapper.text()).toContain(`Mon Wed Fri ${wrapper.vm.convertTime(lectureInfo.start)} - ${wrapper.vm.convertTime(lectureInfo.end)}`);
    expect(wrapper.text()).toContain(`Tue Thu ${wrapper.vm.convertTime(tutorialInfo.start)} - ${wrapper.vm.convertTime(tutorialInfo.end)}`);
  });

  it('converts time format correctly', () => {
    expect(wrapper.vm.convertTime(9)).toBe('9:00am');
    expect(wrapper.vm.convertTime(13.5)).toBe('1:30pm');
  });

  it('renders dropdown on initial load as closed', () => {
    expect(wrapper.vm.dropDownVisible).toBe(false);
  });

  it('changes dropdown visibility on toggle', async () => {
    await wrapper.vm.toggleDropdown();
    expect(wrapper.vm.dropDownVisible).toBe(true);
  });
});

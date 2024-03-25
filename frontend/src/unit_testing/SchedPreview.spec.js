import { mount } from '@vue/test-utils';
import SchedPreview from '@/components/SchedPreview.vue';

describe('SchedPreview.vue', () => {
  const propsData = {
    schedule: [
      {
        Lecture: {
          days: ['M', 'W', 'F'],
          start: 8,
          end: 9.5,
          LectureNO: '101'
        },
        courseCode: 'ENG101'
      },
      {
        Lecture: {
          days: ['T', 'R'],
          start: 10,
          end: 11.5,
          LectureNO: '201'
        },
        courseCode: 'MATH101'
      }
    ]
  };

  let wrapper;
  beforeEach(() => {
    wrapper = mount(SchedPreview, { propsData });
  });

  it('renders a schedule grid', () => {
    expect(wrapper.findAll('.flex-row').length).toBeGreaterThan(0); 
  });

  it('displays days of the week', () => {
    const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    days.forEach(day => {
      expect(wrapper.text()).toContain(day);
    });
  });

  it('displays time slots correctly', () => {
    const times = ['8am', '9am', '10am', '11am', '12pm'];
    times.forEach(time => {
      expect(wrapper.text()).toContain(time);
    });
  });

  it('renders course blocks for each scheduled class', () => {
    expect(wrapper.findAll('.absolute.w-sched').length).toBe(propsData.schedule.length); 
  });


  it('applies correct color styles for different classes', () => {
    const courseBlocks = wrapper.findAll('.absolute.w-sched div');
    expect(courseBlocks.at(0).attributes('class')).toContain('bg-course-100'); 
  });
});

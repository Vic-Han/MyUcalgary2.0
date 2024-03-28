import { mount } from '@vue/test-utils';
import CalendarPreview from '@/components/CalendarPreview.vue';

describe('CalendarPreview.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(CalendarPreview);
  });

  it('renders the component with a header', () => {
    expect(wrapper.find('h2').text()).toBe('Important Dates');
  });

  it('displays the correct number of dates', () => {
    const listItems = wrapper.findAll('li');
    expect(listItems.length).toBe(wrapper.vm.importantDates.length);
  });

  it('checks the structure of a list item', () => {
    const firstItem = wrapper.find('li:first-of-type');
    expect(firstItem.find('.font-bold').exists()).toBe(true); // Check for bold font style
    expect(firstItem.find('.text-3xl').exists()).toBe(true); // Check for size
    expect(firstItem.find('.bg-red-500').exists()).toBe(true); // Check for the presence of the color indicator
  });

  it('ensures each item contains month, day, and event text', () => {
    const firstItem = wrapper.find('li:first-of-type');
    const dateInfo = wrapper.vm.importantDates[0]; // First date object from data

    expect(firstItem.text()).toContain(dateInfo.month);
    expect(firstItem.text()).toContain(dateInfo.day);
    expect(firstItem.text()).toContain(dateInfo.event);
  });

  it('verifies the presence of overflow handling', () => {
    expect(wrapper.find('ul').classes()).toContain('overflow-y-auto');
  });

  it('checks for rounded borders and shadow on list items', () => {
    const firstItem = wrapper.find('li:first-of-type');
    expect(firstItem.classes()).toContain('rounded-lg');
    expect(firstItem.classes()).toContain('shadow-lg');
  });
});

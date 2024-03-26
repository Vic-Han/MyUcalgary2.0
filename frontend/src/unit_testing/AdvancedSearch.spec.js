import { mount } from '@vue/test-utils';
import AdvancedSearch from '@/components/AdvancedSearch.vue';

describe('AdvancedSearch.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(AdvancedSearch, {
      // Props if there are any to pass
    });
  });

  it('renders and is visible on mount', () => {
    expect(wrapper.isVisible()).toBe(true);
  });

  it('updates the start time when input is changed', async () => {
    const input = wrapper.find('input#start-time');
    await input.setValue('08:00');
    expect(wrapper.vm.startTime).toBe('08:00');
  });


  it('updates the end time when input is changed', async () => {
    const input = wrapper.find('input#end-time');
    await input.setValue('10:00');
    expect(wrapper.vm.endTime).toBe('10:00');
  });


 
});

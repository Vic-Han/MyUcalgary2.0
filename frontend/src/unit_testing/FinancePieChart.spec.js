import { mount } from '@vue/test-utils';
import FinancePieChart from '@/components/FinancePieChart.vue';

describe('FinancePieChart.vue', () => {
  const propsData = {
    term: 'Fall 2024',
    amount: '1500',
    status: 'Pending',
    due: '2024-09-01'
  };

  let wrapper;
  beforeEach(() => {
    wrapper = mount(FinancePieChart, { propsData });
  });


  it('shows term fees correctly', () => {
    expect(wrapper.text()).toContain(`${propsData.term} Fees`);
  });

  it('displays the correct amount and status', () => {
    expect(wrapper.text()).toContain(`$${propsData.amount}`);
    expect(wrapper.find('.italic').text()).toContain(propsData.status);
  });

  it('displays the due date', () => {
    expect(wrapper.text()).toContain(`Due by: ${propsData.due}`);
  });

  it('shows status icon and color corresponding to the "Pending" status', () => {
    expect(wrapper.find('.fill-yellow-100').exists()).toBe(true);
    expect(wrapper.find('.text-yellow-100').exists()).toBe(true);
  });

  it('updates status icon and color when status changes', async () => {
    await wrapper.setProps({ status: 'Paid' });
    expect(wrapper.find('.fill-green-100').exists()).toBe(true);
    expect(wrapper.find('.text-green-100').exists()).toBe(true);

    await wrapper.setProps({ status: 'Overdue' });
    expect(wrapper.find('.fill-red-100').exists()).toBe(true);
    expect(wrapper.find('.text-red-100').exists()).toBe(true);
  });
});

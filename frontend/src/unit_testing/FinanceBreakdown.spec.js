import { shallowMount } from '@vue/test-utils';
import FinanceBreakdown from '../views/FinanceBreakdown.vue';

const mockFetch = jest.fn().mockImplementation(() =>
  Promise.resolve({
    json: () => Promise.resolve({
      activity: {},
      currentStudentInfo: { selectedTerm: 'Winter 2024', terms: {} },
    }),
  })
);

global.fetch = mockFetch;

describe('FinanceBreakdown.vue', () => {
  let wrapper;

  beforeEach(() => {
    mockFetch.mockClear(); 
    wrapper = shallowMount(FinanceBreakdown, {
      global: {
        mocks: {
          $store: {
            state: {
              serverPath: 'http://localhost'
            }
          },
          $cookies: {
            get: () => 'fake-auth-token'
          }
        }
      }
    });
  });

  it('renders the component correctly', async () => {
    await wrapper.vm.fetchFinancialData();


    expect(wrapper.find('select').exists()).toBe(true); 
    expect(wrapper.findAll('a').length).toBeGreaterThan(0); 
  });

  it('returns the correct payment type for different financial data types', () => {
    expect(wrapper.vm.paymentType('scholarship')).toBe('payment');
    expect(wrapper.vm.paymentType('award')).toBe('payment');
    expect(wrapper.vm.paymentType('payment')).toBe('payment');
    expect(wrapper.vm.paymentType('fee')).toBe('charge');
    expect(wrapper.vm.paymentType('refund')).toBe('refund');
  });

});

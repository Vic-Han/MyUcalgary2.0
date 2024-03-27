import { shallowMount } from '@vue/test-utils';
import DashBoard from '../views/DashBoard.vue';
import CalendarPreview from '../components/CalendarPreview.vue';

jest.mock('../components/CalendarPreview.vue', () => ({
  name: 'CalendarPreview',
  template: '<div></div>'
}));


describe('DashBoard.vue', () => {
    let wrapper;
  
    beforeEach(() => {
      wrapper = shallowMount(DashBoard, {
        global: {
          mocks: {
            $store: {
              state: {
                serverPath: 'http://localhost'
              }
            },
            $cookies: {
              get: () => 'fake-auth-token'
            },
            $http: {
              get: jest.fn().mockResolvedValue({
                data: {}
              })
            }
          },
          stubs: ['router-link']
        }
      });
    });
  
    it('renders the component correctly', () => {
      expect(wrapper.exists()).toBe(true);
      expect(wrapper.findComponent(CalendarPreview).exists()).toBe(true);
    });
  });
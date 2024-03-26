import { shallowMount } from '@vue/test-utils';
import GradeBreakdown from '@/views/GradeBreakdown.vue';
import { nextTick } from 'vue';

const mockStore = {
  state: {
    serverPath: 'http://localhost'
  }
};

const globalMocks = {
  mocks: {
    $store: mockStore,
    $cookies: {
      get: () => "fake-auth-token"
    },
    $http: {
      get: () => Promise.resolve({
        data: {
          overallGPA: "3.5",
          letterGrade: "A",
          activity: {},
          currentStudentInfo: {}
        }
      })
    }
  }
};

describe('GradeBreakdown.vue', () => {
  it('renders and displays GPA correctly', async () => {
    const wrapper = shallowMount(GradeBreakdown, {
      global: globalMocks
    });
    await wrapper.vm.$nextTick();

    expect(wrapper.text()).toContain('Cumulative GPA');
    expect(wrapper.text()).toContain('3.5');
  });
});
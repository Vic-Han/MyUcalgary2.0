import { shallowMount } from '@vue/test-utils'; 
import LoginScreen from '../views/LoginScreen.vue';
import { createRouter, createWebHistory } from 'vue-router';
import { createStore } from 'vuex';

const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/', component: { template: '<div />' } }]
});

const store = createStore({
  state: {
    serverPath: 'http://localhost'
  }
});

const cookies = {
  get: jest.fn(),
  set: jest.fn()
};

const http = {
  post: jest.fn()
};

describe('LoginScreen.vue', () => {
  let wrapper;

  beforeEach(async () => {
    wrapper = shallowMount(LoginScreen, {
      global: {
        mocks: {
          $cookies: cookies,
          $http: http
        },
        plugins: [router, store]
      }
    });
    await router.isReady();
  });

  it('renders without errors', () => {
    expect(wrapper.exists()).toBeTruthy();
  });

  it('has a login button', () => {
    const loginButton = wrapper.find('.text-red-100'); 
    expect(loginButton.exists()).toBe(true);
  });

});

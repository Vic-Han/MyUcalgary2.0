import { mount } from '@vue/test-utils';
import ProfilePreview from '@/components/ProfilePreview.vue';
import { createRouter, createWebHistory } from 'vue-router';


const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/profile', name: 'profile' }] 
});


const mockCookies = {
  get: jest.fn().mockReturnValue('JD')
};

describe('ProfilePreview.vue', () => {
  const wrapper = mount(ProfilePreview, {
    global: {
      mocks: {
        $cookies: mockCookies
      },
      plugins: [router]
    }
  });

  it('displays initials correctly', () => {
    expect(wrapper.text()).toContain('JD'); 
  });

});

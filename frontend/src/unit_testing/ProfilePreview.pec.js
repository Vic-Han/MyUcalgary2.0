import { mount } from '@vue/test-utils';
import ProfilePreview from '@/components/ProfilePreview.vue';
import VueRouter from 'vue-router';

// Mock Vue Router
const router = new VueRouter({
  routes: [{ path: '/profile', name: 'profile' }] // 匹配到您的个人资料路由
});

// Mock cookies
const mockCookies = {
  get: jest.fn().mockReturnValue('JD') // 假设用户缩写为 'JD'
};

describe('ProfilePreview.vue', () => {
  // 使用 mock 的 cookies 之前，您需要确保全局可以访问到这个 mock 对象
  // 以下是使用 mount 挂载组件时的一种方式
  const wrapper = mount(ProfilePreview, {
    global: {
      mocks: {
        $cookies: mockCookies
      },
      plugins: [router]
    }
  });

  it('renders a link to the profile page', () => {
    expect(wrapper.find('router-link').exists()).toBe(true);
    expect(wrapper.find('router-link').attributes('to')).toBe('/profile');
  });

  it('displays initials correctly', () => {
    expect(wrapper.text()).toContain('JD'); // 检查是否显示了正确的缩写
  });

  it('has correct styling for the initials container', () => {
    const initialsContainer = wrapper.find('.rounded-full');
    expect(initialsContainer.exists()).toBe(true);
    expect(initialsContainer.classes()).toContain('bg-gray-100'); // 检查背景色
    expect(initialsContainer.classes()).toContain('border-rubine-100'); // 检查边框颜色
  });

  it('calls cookies.get with "initials" key on created hook', () => {
    expect(mockCookies.get).toHaveBeenCalledWith('initials');
  });
});

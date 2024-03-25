import { mount } from '@vue/test-utils';
import ProfilePreview from '@/components/ProfilePreview.vue';
import { createRouter, createWebHistory } from 'vue-router';

// 创建 Vue Router 实例
const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/profile', name: 'profile' }] // 匹配到您的个人资料路由
});

// Mock cookies
const mockCookies = {
  get: jest.fn().mockReturnValue('JD') // 假设用户缩写为 'JD'
};

describe('ProfilePreview.vue', () => {
  // 挂载组件
  const wrapper = mount(ProfilePreview, {
    global: {
      mocks: {
        $cookies: mockCookies
      },
      plugins: [router]
    }
  });

  it('displays initials correctly', () => {
    expect(wrapper.text()).toContain('JD'); // 检查是否显示了正确的缩写
  });

  // 这里可以继续添加其他测试用例
});

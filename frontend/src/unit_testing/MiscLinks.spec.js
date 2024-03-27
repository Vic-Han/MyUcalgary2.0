import { shallowMount } from '@vue/test-utils';
import MiscLinks from '@/views/MiscLinks.vue';

describe('MiscLinks.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(MiscLinks, {
    });
  });

  it('renders all sections correctly', () => {
    const sections = ['Get Involved', 'Get Around', 'Help & Support', 'Get Connected'];
    sections.forEach(section => {
      expect(wrapper.text()).toContain(section);
    });
  });

  it('checks the presence of links and their classification', () => {
    const categories = ['Events at UCalgary', 'Find a Faculty', 'Account Management', 'UCalgary Webmail'];
    categories.forEach(category => {
      expect(wrapper.html()).toContain(category);
    });
  });

  it('verifies external links open in a new tab', () => {
    const links = wrapper.findAll('a[target="_blank"]');
    expect(links.length).toBeGreaterThan(0);
  });
});

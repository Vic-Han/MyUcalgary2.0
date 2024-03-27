import { mount } from '@vue/test-utils';
import ApplicationSummary from '@/components/ApplicationSummary.vue';

describe('ApplicationSummary.vue', () => {
  const applicationData = {
    id: '123',
    status: 'Pending',
    applicantName: 'John Doe',
    submissionDate: '2024-03-25'
  };

  it('should mount the component', () => {
    const wrapper = mount(ApplicationSummary, {
      propsData: { application: applicationData }
    });
    expect(wrapper.isVisible()).toBe(true);
  });

  it('displays the application data correctly', () => {
    const wrapper = mount(ApplicationSummary, {
      propsData: { application: applicationData }
    });
    expect(wrapper.text()).toContain(applicationData.applicantName);
    expect(wrapper.text()).toContain(applicationData.status);
    expect(wrapper.text()).toContain(applicationData.submissionDate);
  });

  it('has the correct prop type for application', () => {
    const wrapper = mount(ApplicationSummary, {
      propsData: { application: applicationData }
    });
    const applicationProp = wrapper.vm.$options.props.application;
    expect(applicationProp.required).toBeTruthy();
    expect(applicationProp.type).toBe(Object);
  });

  it('renders the initial message correctly', () => {
    const wrapper = mount(ApplicationSummary, {
      propsData: { application: applicationData }
    });
    expect(wrapper.text()).toContain('This is the ApplicationSummary Component');
  });
});

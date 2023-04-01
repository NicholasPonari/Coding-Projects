import Layout from "../components/Layout";
import Header from "../components/Header";
import Hero from "../components/Hero";
import Feature from "../components/Feature";
import Service from "../components/Service";
import About from "../components/About";
import Footer from "../components/Footer";
const Index = () => {
  return (
    <Layout pageTitle="Welcome to WeTF, the world's first community-managed fund">
      <Header />
      <Hero />
      <Feature />
      <Service />
      <About />
      <Footer />
    </Layout>
  );
};
export default Index;

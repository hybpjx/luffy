<template>
  <div class="home">
    <Header></Header>
    <Banner></Banner>
    <Footer></Footer>

  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import Header from "@/components/common/Header";
// eslint-disable-next-line no-unused-vars
import Banner from "@/components/common/Banner";
// eslint-disable-next-line no-unused-vars
import Footer from "@/components/common/Footer";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  components: {
    Header,
    Banner,
    Footer,
  }
}
</script>

<style scoped>

</style>
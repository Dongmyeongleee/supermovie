<template>
  <div
    id="carouselExampleCaptions"
    class="carousel slide"
    data-bs-ride="carousel"
  >
  
    <div class="carousel-indicators">
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <div class="carousel-caption d-none d-md-block">
          <h1>타짜</h1>
          <!-- <h4>Have a happy movie</h4> -->
        </div>
        <img
          src="@/고니.png"
          class="d-block w-100"
          style="height: 700px"
        />
      </div>
      <div class="carousel-item">
        <img
          src="@/동작그만.png"
          class="d-block w-100"
          style="height: 700px"
        />
        <div class="carousel-caption d-none d-md-block">
          <!-- <h1>supermovie</h1>
          <h4>Have a happy movie</h4> -->
        </div>
      </div>
      <div class="carousel-item">
        <img
          src="@/쫄뒈.png"
          class="d-block w-100"
          style="height: 700px"
        />
        <div class="carousel-caption d-none d-md-block">
          <!-- <h1>supermovie</h1>
          <h4>Have a happy movie</h4> -->
        </div>
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleCaptions"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleCaptions"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>
<script>
export default {
  name: "Home",
  methods: {},
};
</script>

<style>
.row {
  justify-content: center;
  justify-items: center;
  margin: 50px;
  width: 90%;
}
</style>
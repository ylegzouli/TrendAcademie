<script>

    function getBasename(filename) {
        return filename.split('.').slice(0, -1).join('.');
    }

    const images = [
        "sephora0.webp",
        "sephora1.webp",
        "sephora2.webp",
        "sephora3.webp",
        "sephora4.webp"
    ]

</script>
<div class="main-container">

<div class="navbar rounded-box" style="background-color: white;">
  <div class="flex justify-center w-full title" style="font-family: 'Gill Sans'">
    <div class="text-lg" style="font-size: 24px;">S E P H O R A</div>
  </div>
  </div><br>

  <div class="timeline-select-container">
  <select class="select select-bordered select-xs max-w-xs">
    <option selected>Month</option>
    <option>Week</option>
    <option>Day</option>
  </select>
  </div>

<br>
<br>
<br>

<h1 class="text-lg" style="font-family:'Gill Sans'">TOP PRODUCTS</h1>

<div class="carousel rounded-box">
    {#each images as image}
      <div class="carousel-item">
          <a href="product/{getBasename(image)}">
            <img src={image} alt="foo" />
            <div class="stat">
              <div class="stat-figure text-primary">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
              </div>
              <div>Total Likes</div>
              <div class="stat-value text-primary">25.6K</div>

              <div class="stat-title">Total mentions</div>
              <div class="stat-value text-primary">25</div>
              
            </div>
        </a>
      </div>
    {/each}
</div>

<h1 class="text-lg" style="font-family:'Gill Sans'">TOP BRANDS</h1>
<div class="carousel rounded-box">
  {#each images as image}
      <a href="product/{getBasename(image)}" class="carousel-item">
          <img src={image} alt="foo" />
      </a>

  {/each}
</div>

</div>

<style>

/* .navbar .flex.justify-center { */
    /* margin-bottom: 1px; Add bottom margin to the SEPHORA title div */
/* } */

.timeline-select-container {
    display: flex;
    justify-content: flex-end; /* Aligns the child element to the right */
    margin-right: 20px; /* Optional: Adds some right margin */
}

/* Targeting the h1 tag with "PRODUCTS" */
h1{
    margin-left: 7px; /* Add left margin to the h1 tag */
}

.carousel {
    /* border: 1px solid #000; Add border to the entire carousel */
    padding: 10px; /* Add padding inside the carousel */
    margin: 0 auto; /* Center the carousel if needed */
    margin-bottom: 10px; /* Add bottom margin to the h1 tag */
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; 
}

.carousel-item {
    flex: 0 0 auto;
    border: 1px solid #ccc; /* Add border to each carousel item */
    margin-right: 20px; /* Add space between items */
    /* Additional styles for carousel item */
    padding: 10px;
}

.carousel-item img {
    width: 150px; /* Adjust width as needed */
    height: auto; 
    display: block;
}     

.carousel-item:last-child {
    margin-right: 0; /* Remove right margin from the last item */
}

.main-container {
    margin-top: 20px; /* Top margin */
    margin-left: 20px; /* Left margin */
    margin-right: 20px; /* Right margin */
    /* Adjust the values as needed */
}


</style>

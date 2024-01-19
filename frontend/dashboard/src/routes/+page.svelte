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
        <a href="product/{getBasename(image)}" class="carousel-item">
            <img src={image} alt="foo" />
        </a>
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
}

.carousel-item {
    border: 1px solid #ccc; /* Add border to each carousel item */
    margin-right: 20px; /* Add space between items */
    /* Additional styles for carousel item */
}

.carousel-item img {
    width: 150px; /* Adjust width as needed */
    height: auto; /* Maintain aspect ratio */
    display: block; /* Ensure img takes the full width of its container */
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

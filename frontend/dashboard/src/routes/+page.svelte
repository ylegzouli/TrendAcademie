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

<div class="navbar rounded-box" style="background-color: white;">
  <div class="flex justify-center w-full" style="font-family: 'Gill Sans'">
    <div class="text-lg" style="font-size: 24px;">S E P H O R A</div>
  </div>
  </div><br>
  <div class="flex justify-end flex-1 px-2">
    <div class="flex items-stretch">
      <!-- <a class="btn btn-ghost rounded-btn">Button</a> -->
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost rounded-btn">Select by timeline</div>
        <ul tabindex="0" class="menu dropdown-content z-[1] p-2 shadow bg-base-100 rounded-box w-52 mt-4">
          <li><a>Week</a></li>
          <li><a>Month</a></li>
          <li><a>Year</a></li>
        </ul>
      </div>
    </div>
  </div>

<br>
<br>
<br>

<h1 class="text-lg font-bold">PRODUCTS</h1>

<div class="carousel rounded-box">
    {#each images as image}
        <a href="product/{getBasename(image)}" class="carousel-item">
            <img src={image} alt="foo" />
        </a>
    {/each}
</div>


<style>
    .carousel-item {
      border-right: 1px solid #000; /* Change color as needed */
    }

    .carousel-item:last-child {
      border-right: none; /* Remove border from the last item */
    }

</style>

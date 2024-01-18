<script>
    const images = [
        "sephora0.webp",
        "sephora1.webp",
        "sephora2.webp",
        "sephora3.webp",
        "sephora4.webp"
    ]
</script>

<div class="navbar bg-base-300 rounded-box">
    <div class="flex-1 px-2 lg:flex-none">
      <a class="text-lg font-bold">Dashboard</a>
    </div>
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
  </div><br>

<br>
<br>
<br>

<h1 class="text-lg font-bold">PRODUCTS</h1>
<div class="carousel rounded-box">
    {#each images as image}
        <!-- <a href="" class="carousel-item"> -->
        <div class="carousel-item">
            <img src={image} alt="foo" />
        </div>
    {/each}
</div>

<!--
<br>
<br>
<br>
<br>

<h1 class="text-lg font-bold">PRODUCTS</h1>

<div class="carousel rounded-box">
    <a href="" class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.jpg" alt="Burger" />
    </a>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1494253109108-2e30c049369b.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1559181567-c3190ca9959b.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.jpg" alt="Burger" />
    </div>
  </div>

<br>
<br>
<br>
<br>

<h1 class="text-lg font-bold">BRANDS</h1>

<div class="carousel rounded-box">
    <a href="" class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.jpg" alt="Burger" />
    </a>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1494253109108-2e30c049369b.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1559181567-c3190ca9959b.jpg" alt="Burger" />
    </div>
    <div class="carousel-item">
      <img src="https://daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.jpg" alt="Burger" />
    </div>
  </div>
-->

<style>
    .carousel-item {
      border-right: 1px solid #000; /* Change color as needed */
    }

    .carousel-item:last-child {
      border-right: none; /* Remove border from the last item */
    }
</style>

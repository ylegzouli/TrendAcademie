<script lang="ts">
    import axios from "axios";
    import { onMount } from "svelte";

    type Product = {
        product_id: string
        product_name: string
        product_image: string
    };

    type Brand = {
        brand_id: string
        brand_name: string
        brand_image: string
    };

    let brands: Brand[] = [];
    let products: Product[] = [];

    async function init() {
        try {
            const response = await axios.get('http://localhost:8000/home/foo')
            console.log('init success')
            brands = response.data.brands
            products = response.data.products
            console.log(brands)
            console.log(products)
        } catch (e) {
            console.log('init failure')
            console.log(e)
        }
    }

    onMount(init);

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
    {#each products as product}
        <a href="product/{product.product_id}" class="carousel-item">
            <img src={product.product_image} alt="foo" />
        </a>
    {/each}
</div>

<br>
<br>
<br>

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

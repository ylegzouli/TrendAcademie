<script lang="ts">
    import axios from "axios";
    import { onMount } from "svelte";

    type Product = {
        product_id: string
        product_name: string
        product_image: string
        product_mentions: string
        product_likes: string
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
      <div class="carousel-item">
        <a href="product/{product.product_id}">
            <div class="card w-96 bg-base-100 shadow-xl">
                <figure><img src={product.product_image} alt="Shoes" /></figure>
                <div class="card-body">
                    <div class="stat">
                      <div class="stat-figure text-primary">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                      </div>
                      <div class="stat-title">Media Likes</div>
                      <div class="stat-value text-primary">{product.product_likes}K</div>
                      <div class="stat-title">Media Mentions</div>
                      <div class="stat-value text-primary">{product.product_mentions}</div>
                    </div>
                  <div class="card-actions justify-end">
                  </div>
                </div>
            </div>
        </a>
      </div>
    {/each}
</div>
<br>

<br>
<br>
<br>

<!-- <h1 class="text-lg" style="font-family:'Gill Sans'">Brief</h1> -->
<textarea class="textarea textarea-bordered" placeholder="Brief"></textarea>

</div>

<style>

/* .navbar .flex.justify-center { */
    /* margin-bottom: 1px; Add bottom margin to the SEPHORA title div */
/* } */

.stat-value.text-primary {
    color: black !important;
    font-family: 'Gill Sans';
}

.stat-figure svg {
    stroke: rgb(173, 120, 129) !important;
}

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
    /* border: 1px solid #ccc; */
    margin-right: 5px; /* Add space between items */
    /* Additional styles for carousel item */
    padding: 2px;
}

.carousel-item img {
    width: 140px; /* Adjust width as needed */
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

.textarea {
    width: 100%; /* This will make the textarea take full width of its container */
    height: 200px; /* Set the height in pixels as per your preference */
    /* Add any other styles you need */
}


</style>

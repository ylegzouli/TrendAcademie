<script lang="ts">
    import axios from "axios";
    import { onMount } from "svelte";
    import arrow from '$lib/assets/arrow-back-ios.svg'

    type Product = {
        product_id: string
        product_name: string
        product_image: string
        product_mentions: string
        product_likes: string
        product_brand: string
    };

    type Brand = {
        brand_id: string
        brand_name: string
        brand_image: string
    };

    let brands: Brand[] = [];
    let products: Product[] = [];
    let selectedTimeline: string = 'Month'; // Default value

    async function init(timeline: string) {
        try {
            const response = await axios.get("http://localhost:8000/home/" + timeline.toLowerCase())
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

    // Reactive statement to watch for changes in the selected timeline
    $: {
        if (selectedTimeline) {
            init(selectedTimeline);
        }
    }

    onMount(init(selectedTimeline));

    // Function to truncate product name
    function displayProductName(productName: string): string {
        return productName.length > 27 ? `${productName.substring(0, 27)} ...` : productName;
    }

</script>

<div class="main-container">

    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <a href="/">
                <img src={arrow} alt="back icon"/>
            </a>
        </div>
        <div class="navbar-center">
          <div class="text-lg" style="font-size: 24px;">S E P H O R A</div>
        </div>
        <div class="navbar-end">
            <div class="timeline-select-container">
            <select class="select select-bordered select-sm max-w-xs" bind:value={selectedTimeline}>
              <option selected>Month</option>
              <option>Week</option>
              <option>Day</option>
            </select>
          </div>
        </div>
      </div>

    <br>
    <br>

<h1 class="text-lg top-title" style="font-family:'Gill Sans'">TOP PRODUCTS</h1>
<br>
<div class="carousel rounded-box">
    {#each products as product}
      <div class="carousel-item">
          <a href="product/{product.product_id}">
          <div class="card w-96 bg-base-100 shadow-xl">
              <figure><img src={product.product_image} alt="Shoes" /></figure>
            <div class="card-body">
              <p>{product?.product_brand}</p>
              <h2 class="card-title">{displayProductName(product?.product_name)}</h2>
                <div class="stat">
                  <div class="stats shadow" style="overflow: hidden;">
                    <div class="stat">
                      <div class="stat-figure text-secondary">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                      </div>
                      <div class="stat-value text-secondary">{product?.product_mentions}</div>
                      <div class="stat-desc">mentions on social media</div>
                    </div>
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
<textarea class="textarea textarea-bordered" placeholder="Brief"></textarea>
</div>

<style>

.stat-value {
    color: rgb(90, 88, 88) !important;
}

.stat-figure svg {
    stroke: rgb(199, 0, 33) !important;
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
    /* border: 1px solid #000; */
    padding: 10px; /* Add padding inside the carousel */
    margin: 0 auto; /* Center the carousel if needed */
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.carousel-item {
    flex: 0 0 auto;
    margin-right: 5px; /* Add space between items */
    padding: 2px;
}

.carousel-item img {
    width: 200px; /* Adjust width as needed */
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
}

.textarea {
    width: 100%; /* This will make the textarea take full width of its container */
    height: 200px; /* Set the height in pixels as per your preference */
}

.top-title {
    margin-left: 30px; /* Add left margin to the h1 tag */
}


</style>

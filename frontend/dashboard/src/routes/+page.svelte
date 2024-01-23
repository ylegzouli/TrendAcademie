<script lang="ts">
    import axios from "axios";
    import { influencers } from '../store.ts';
    import wallpaper from '$lib/assets/sephora_wallpaper.jpg'

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
    let startup: boolean = true

    async function init(timeline: string) {
        try {
            const response = await axios.get("http://localhost:8000/home/" + timeline.toLowerCase())
            console.log('init success')
            brands = response.data.brands
            products = response.data.products
            influencers.set(response.data.influencers);
            console.log(response.data)
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

    // Function to truncate product name
    function displayProductName(productName: string): string {
        return productName.length > 23 ? `${productName.substring(0, 23)} ...` : productName;
    }

    function handleClick() {
        startup = false;
    }

</script>

<div class={startup ? 'landing' : 'hidden'} style="background-image: url({wallpaper});">
    <button class="btn btn-wide transparent" on:click={handleClick}>ENTER</button>
</div>

<div class={startup ? 'hidden' : ''}>
<div class="main-container">

    <div class="navbar bg-base-100">
        <div class="navbar-start">

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

<h1 class="text-lg top-title" style="font-family:'Gill Sans'">TOP INFLUENCERS</h1>
<br>
<div class="carousel rounded-box">
    {#each $influencers as influencer}
      <div class="carousel-item">
          <a href="influencer/{influencer.name}">
          <div class="card w-96 bg-base-100 shadow-xl">
            <figure>
                <img class="mask mask-circle" src="http://localhost:8000/images/{influencer.name}" alt="ProfilePicture"/>
            </figure>
            <div class="card-body">
                <div style="display: flex;">
                    <img src="/tiktok.png" alt="tiktok" style="width: 20px; height: 20px; margin-right: 5px;"/>
                    @{influencer.name}
                </div>
                <div style="display: flex;">
                    <img src="/instagram.png" alt="tiktok" style="width: 20px; height: 20px; margin-right: 5px;"/>
                    @{influencer.name}
                </div>
                <div class="stat">
                    <div class="stats shadow" style="overflow: hidden;">
                      <div class="stat">
                        <div class="stat-figure text-primary">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                          </div>


                        <div class="stat-value text-secondary">{influencer.likes /1000}k</div>
                        <div class="stat-desc">likes on products mention</div>
                      </div>
                    </div>
                <!-- <p>{influencer?.likes} likes</p> -->
            </div>
        </div>
      </a>
      </div>
    {/each}
</div>

<br>
<br>

<!-- <textarea class="textarea textarea-bordered" placeholder="Brief"></textarea> -->
</div>
</div>

<style>

button.transparent {
    background: transparent;
    color: #fff; /* Adjust color as needed */
    border: 1px solid #fff; /* Adjust border color as needed */
}

.landing {
    background-size: cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

    .hidden {
    display: none;
}

button {
    padding: 10px 20px;
    font-size: 1.5em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 150px;
}

.main-container {
    margin-top: 2%;
    margin-left: 2%;
    margin-right: 2%;

}

.stat-value {
    font-size: 140%; /* Smaller font size for the stat value */
    color: rgb(90, 88, 88) !important;

}

.stat-desc {
    font-size: 70%; /* Smaller font size for the stat description */
}

.stat-figure svg {
    width: 50%; /* Smaller width for the SVG */
    height: auto; /* Height will scale automatically */
    stroke: rgb(199, 0, 33) !important;
}

.timeline-select-container {
    display: flex;
    justify-content: flex-end; /* Aligns the child element to the right */
    margin-right: 1%; /* Optional: Adds some right margin */
}

/* Targeting the h1 tag with "PRODUCTS" */
h1{
    margin-left: 4%; /* Add left margin to the h1 tag */
}

.carousel {
    /* border: 1px solid #000; */
    padding: 1%; /* Add padding inside the carousel */
    margin: 0 auto; /* Center the carousel if needed */
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.carousel-item {
    flex: 0 0 auto;
    margin-right: 1%;
    /* padding: 2%; */
    border-radius: 3%;

    /* width: 45%; */
    /* margin-right: 2%; */
    padding: 1%;
    border-radius: 3%;
    box-sizing: border-box;


}

.carousel-item img {
    width: 35%; /* Adjust width as needed */
    height: auto;
    display: block;
}

.carousel-item:last-child {
    margin-right: 0; /* Remove right margin from the last item */
}


.top-title {
    margin-left: 30px; /* Add left margin to the h1 tag */
}

.card-title {
    font-size: 18px; /* Smaller font size for the card title */
}

.stats {
    padding: 0.5%; /* Reduced padding inside the stats */
}

.stat {
    margin: 0.5% 0; /* Reduced vertical margin for each stat */
}

/* Additional adjustment to the container of the stats if necessary */
.stats.shadow {
    width: 90%; /* Adjust width of the stat container */
    margin: auto; /* Center the stat container if needed */
}

</style>

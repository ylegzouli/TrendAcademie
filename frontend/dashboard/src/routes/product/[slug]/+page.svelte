<script lang="ts">
    import { onDestroy } from 'svelte';
    import { page } from '$app/stores';
    import axios from 'axios';
    import arrow from '$lib/assets/arrow-back-ios.svg'
    import Plot from 'svelte-plotly.js';


    let slug: any;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);

    let productData: any
    let data: any = [
      {
        x: [],
        y: [],
      }
    ];
    let selectedTimeline: string = 'Month'; // Default value

    async function init(timeline: string) {
        try {
            const response = await axios.get("http://localhost:8000/product/" + timeline.toLowerCase() + "/" + slug)

            console.log('init success')
            // console.log(response.data)
            productData = response.data
            data = [
              {
                x: productData?.chart_x,
                y: productData?.chart_y,
              }
            ];

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
        return productName.length > 27 ? `${productName.substring(0, 27)}...` : productName;
    }

      // Function to truncate product name
      function displayInstaName(productName: string): string {
        return productName.length > 12 ? `${productName.substring(0, 12)}...` : productName;
    }

  function formatNumber(numStr) {
    const num = parseFloat(numStr);
    return !isNaN(num) ? num.toFixed(1) : '0.0';
  }


</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<div class="main-container">

    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <a href="/">
                <img src={arrow} alt="back icon"/>
            </a>
        </div>
        <div class="navbar-center">
          <div class="text-lg" style="font-size: 20px;">S E P H O R A</div>
        </div>
        <div class="navbar-end">

        </div>
      </div>

    <br>
    <br>

    <div class="product-container">

      <div class="card lg:card-side bg-base-100 shadow-xl">

        <div class="rank-container">
          <span class="fa fa-star checked"></span>
          <span class="rank-number">{productData?.rank}</span>
        </div>

        <figure><img src={productData?.image} alt="Album"/></figure>
        <div class="card-body">
          <p class="description">{productData?.brand}</p>
          <h2 class="card-title">{productData?.name}</h2>
          <p class="description">{productData?.description}</p>
          
          <br>

          <div class="grid gap-4 grid-cols-2">
            
            <div>
            <div class="stat shadow">
                <img src="/instagram.png" alt="Shoes" width="60" height="60" style=""/>
            </div>
            </div>


            <div>
              <div class="stat shadow">
                <div class="stat-figure text-secondary">
                  <div class="avatar online">
                  </div>
                </div>
                <div class="stat-title">Most share by</div>
                {#if productData?.influencer}
                {#each productData.influencer.slice(0, 2) as influencer, index}
                    <span style="color:cornflowerblue; font-size: 77%;">@{displayInstaName(influencer)}</span>
                {/each}
                {/if}
              </div>
            </div>


            <div>
              <div class="stat shadow">
                <div class="stat-figure text-primary">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                </div>
                <div class="stat-title">Likes</div>
                <div class="stat-value text-primary">{formatNumber(productData?.likes)}K</div>
              </div>
            </div>

            <div>
              <div class="stat shadow">
                <div class="stat-figure text-secondary">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <div class="stat-title">Comment</div>
                <div class="stat-value text-secondary">{productData?.comment}K</div>
              </div>
            </div>


          </div>
        <br>

        </div> 
      </div> 

  </div> 

    <h1 class="text-lg" style="font-family:'Gill Sans'">Similar Products</h1>


    <div class="carousel rounded-box">
        {#if productData?.similar}
        {#each productData.similar as similar}
          <div class="carousel-item">
            <a href={`${window.location.origin}/product/${similar?.idx}`}>
                <div class="card w-96 bg-base-100 shadow-xl">
                    <figure><img src={similar?.image_url} alt="Shoes" /></figure>
                    <div class="card-body">
                  <p>{similar?.brand}</p>
                  <h2 class="card-title">{displayProductName(similar?.name)}</h2>
                      <div class="card-actions justify-end">
                      </div>
                    </div>
                </div>
            </a>
          </div>
        {/each}
        {/if}
    </div>

    <h1 class="text-lg" style="font-family:'Gill Sans'">Complementary Products</h1>

    <div class="carousel rounded-box">
      {#if productData?.compatible}
      {#each productData.compatible as compatible}
        {#if productData?.name != compatible?.name}
        <div class="carousel-item">
          <a href="{compatible?.idx}">
              <div class="card w-96 bg-base-100 shadow-xl">
                  <figure><img src={compatible?.image_url} alt="Shoes" /></figure>
                  <div class="card-body">
                  <p>{compatible?.brand}</p>
                  <h2 class="card-title">{displayProductName(compatible?.name)}</h2>
                    <div class="card-actions justify-end">
                    </div>
                  </div>
              </div>
          </a>
        </div>
        {/if}
      {/each}
      {/if}
  </div>


</div>

<div style="margin-right: 5%;">
<Plot
  {data}
  layout={{
    margin: { t: 0 },
    yaxis: { autorange: 'reversed' }
  }}
  fillParent='width'
  debounce={250}
/>
</div>

<style>

.rank-container {
    position: absolute;
    top: 0; /* Position it at the top */
    left: 0; /* Position it at the left */
    display: inline-flex;
    align-items: center;
    justify-content: center;
    z-index: 2; /* Ensure it's above other content */
}

.rank-number {
    position: absolute;
    color: black;
    font-size: 16px; /* Adjust as needed */
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;
}

.checked {
    color: rgb(253, 193, 81);
    /* color: rgb(218, 216, 216); */
    font-size: 400%; /* Adjust as needed */
    z-index: 0;
}


.stat-title{
    font-size: 12px;
    margin-bottom: 3%;
}

.stat-value {
    margin: 0;
    font-size: 130%; 
    color: rgb(90, 88, 88) !important;
}

.stat-figure svg {
    stroke: rgb(199, 0, 33) !important;
}

  .main-container {
    margin-top: 2%; /* Top margin */
    margin-left: 2%; /* Left margin */
    margin-right: 2%; /* Right margin */
  }

  .product-container {
    margin-bottom: 50px;
  }

.timeline-select-container {
    display: flex;
    justify-content: flex-end; /* Aligns the child element to the right */
    margin-right: 20px; /* Optional: Adds some right margin */
}

  .product-container figure img {
    max-width: 50%;
    height: auto;
  }

  .description {
    font-size: 13px;
  }

.card-title {
    font-size: 16px;
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
  </style>
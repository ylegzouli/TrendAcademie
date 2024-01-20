<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    import axios from 'axios';
    import arrow from '$lib/assets/arrow-back-ios.svg'

    let slug: any;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);

    // type ProductData = {
    //     name: string
    //     brand: string
    //     image: string // link
    //     description: string
    //     influencer: string
    //     in_stock: string // bool
    //     similar: [string]
    //     compatible: [string]
    //     categories: [string]
    //     highlights: [string]
    //     likes: string
    //     mentions: string
    //     // rank (?)
    // }

    // let productData: productData
    let productData: any
    let selectedTimeline: string = 'Month'; // Default value

    async function init(timeline: string) {
        try {
            const response = await axios.get("http://localhost:8000/product/" + timeline.toLowerCase() + "/" + slug)

            console.log('init success')
            console.log(response.data)
            productData = response.data
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

    onMount(() => init(selectedTimeline));

    let compatible = [
        "https://daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.jpg",
        "https://daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.jpg",
        "https://daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.jpg",
        "https://daisyui.com/images/stock/photo-1494253109108-2e30c049369b.jpg",
        "https://daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.jpg",
        "https://daisyui.com/images/stock/photo-1559181567-c3190ca9959b.jpg",
        "https://daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.jpg"
    ]

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

    <div class="product-container">

      <div class="card lg:card-side bg-base-100 shadow-xl">
        <figure><img src={productData?.image} alt="Album"/></figure>
        <div class="card-body">
          <p>{productData?.brand}</p>
          <h2 class="card-title">{productData?.name}</h2>
          <p>{productData?.description}</p>
          <br>
          <div class="stats shadow" style="overflow: hidden;">

            <div class="stat">
              <div class="stat-figure text-primary">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
              </div>
              <div class="stat-title">Pruduct Likes</div>
              <div class="stat-value text-primary">{productData?.likes}K</div>
              <div class="stat-desc">likes on social media</div>
            </div>

            <div class="stat">
              <div class="stat-figure text-secondary">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              </div>
              <div class="stat-title">Product Comment</div>
              <div class="stat-value text-secondary">{productData?.comment}K</div>
              <div class="stat-desc">comment on social media</div>
            </div>

            <div class="stat">
              <div class="stat-figure text-secondary">
                <div class="avatar online">
                  <div class="w-16 rounded-full">
                    <img src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
                  </div>
                </div>
              </div>
              <div class="stat-title">Share by</div>
              {#if productData?.influencer}
              {#each productData.influencer.slice(0, 3) as influencer, index}
                  <span style="color:cornflowerblue">@{influencer}</span>
              {/each}
          {/if}
            </div>
          </div>

          <div></div>

        </div>
      </div>

  </div>

    <h1 class="text-lg" style="font-family:'Gill Sans'">Similar Products</h1>


    <div class="carousel rounded-box">
        {#each compatible as compatible}
          <div class="carousel-item">
            <a href="product/0">
                <div class="card w-96 bg-base-100 shadow-xl">
                    <figure><img src={compatible} alt="Shoes" /></figure>
                    <div class="card-body">
                      <div class="card-actions justify-end">
                      </div>
                    </div>
                </div>
            </a>
          </div>
        {/each}
    </div>

    <h1 class="text-lg" style="font-family:'Gill Sans'">Complementary Products</h1>


    <div class="carousel rounded-box">
        {#each compatible as compatible}
          <div class="carousel-item">
            <a href="product/0">
                <div class="card w-96 bg-base-100 shadow-xl">
                    <figure><img src={compatible} alt="Shoes" /></figure>
                    <div class="card-body">
                      <div class="card-actions justify-end">
                      </div>
                    </div>
                </div>
            </a>
          </div>
        {/each}
    </div>

</div>

<style>

  .main-container {
    margin-top: 20px; /* Top margin */
    margin-left: 20px; /* Left margin */
    margin-right: 20px; /* Right margin */
    /* font-family: 'Gill Sans'; */
  }

  .product-container {
    /* display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #000;
    padding: 20px; */
    margin-bottom: 50px;
  }

.product-info, .product-image {
  flex: 1 !important ;/* Equal flex grow and shrink */
  flex-basis: 0 !important; /* Starting width */
  box-sizing: border-box !important; /* Include padding and border in the element's total width and height */
  padding: 10px !important;
  max-width: 50% !important; /* Explicitly set max-width to ensure equal width */
}

.timeline-select-container {
    display: flex;
    justify-content: flex-end; /* Aligns the child element to the right */
    margin-right: 20px; /* Optional: Adds some right margin */
}

  /* .product-info {
    flex: 1; */
    /* border: 1px solid #000; */
    /* padding: 10px;
  } */
  /* .product-image {
    flex: 1;
    text-align: right;
    margin-left: 50px;
  } */
  .product-image figure img {
    max-width: 100%;
    height: auto;
  }
  /* .in-stock {
    color: rgb(62, 209, 36);
    * /font-weight: bold; */
  /* } */

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
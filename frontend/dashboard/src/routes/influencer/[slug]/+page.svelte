<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    import axios from 'axios';
    import arrow from '$lib/assets/arrow-back-ios.svg'
    import { influencers } from '../../../store.ts';

    let slug: any;
    const unsubscribe = page.subscribe(({ params }) => {
        slug = params.slug;
    });

    onDestroy(unsubscribe);

    let influencer = $influencers.find(influencer => influencer?.name === slug);

    async function init() {
        console.log('influencer page, store:', $influencers)
    }

    onMount(() => init());

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
        <!-- <div class="navbar-end">
            <div class="timeline-select-container">
            <select class="select select-bordered select-sm max-w-xs" bind:value={selectedTimeline}>
              <option selected>Month</option>
              <option>Week</option>
              <option>Day</option>
            </select>
          </div>
        </div> -->
      </div>

    <br>
    <br>

    <div class="product-container">

      <div class="card lg:card-side bg-base-100 shadow-xl">
        <figure><img src={influencer?.image} alt="Album"/></figure>
        <div class="card-body">
          <h2 class="card-title">{influencer?.name}</h2>
          <br>
          <div class="stats shadow" style="overflow: hidden;">

            <div class="stat">
              <div class="stat-figure text-primary">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
              </div>
              <div class="stat-title">Pruduct Likes</div>
              <!-- <div class="stat-value text-primary">{productData?.likes}K</div> -->
              <div class="stat-value text-primary">0K</div>
              <div class="stat-desc">likes on social media</div>
            </div>

            <div class="stat">
              <div class="stat-figure text-secondary">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              </div>
              <div class="stat-title">Product Comment</div>
              <!-- <div class="stat-value text-secondary">{productData?.comment}K</div> -->
              <div class="stat-value text-secondary">0K</div>
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
              <div class="stat-title">Most share by</div>
              <!-- {#if productData?.influencer}
              {#each productData.influencer.slice(0, 3) as influencer, index}
                  <span style="color:cornflowerblue">@{influencer}</span>
              {/each}
              {/if} -->
            </div>
          </div>
          <br>
        <h1 class="text-lg" style="font-family:'Gill Sans'">Details :</h1>

          <div class="stats shadow" style="overflow: hidden; margin-top: 20px">

            <!-- <div class="stat stat-container">
              <img src="/instagram.png" alt="Shoes" width="50" height="50"/>
                <div class="stat-value text-primary">{productData?.likes}K</div>
            </div>

            <div class="stat stat-container">
              <img src="/tiktok.webp" alt="Shoes" width="50" height="50"/>
                <div class="stat-value text-primary">0.0K</div>
            </div>

            <div class="stat stat-container">
              <img src="/youtube.webp" alt="Shoes" width="50" height="50"/>
                <div class="stat-value text-primary">0.0K</div>
            </div> -->

          </div>
        </div>
      </div>

  </div>

</div>

<style>

.stat-container {
    display: flex;       /* This enables Flexbox */
    align-items: center; /* This aligns items vertically in the center */
    gap: 30px;           /* This adds some space between the image and the text */
}

.stat-value {
    margin: 0; /* You might want to reset margin for alignment, adjust as needed */
}

.main-container {
  margin-top: 20px; /* Top margin */
  margin-left: 20px; /* Left margin */
  margin-right: 20px; /* Right margin */
  /* font-family: 'Gill Sans'; */
}

.product-container {
  margin-bottom: 50px;
}

.product-image figure img {
  max-width: 100%;
  height: auto;
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
<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
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

    function formatFollowersCount(count: any) {
        if (count >= 1000000)
            return (count / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
        if (count >= 1000)
            return (count / 1000).toFixed(1).replace(/\.0$/, '') + 'K';
        return count;
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
        </div>
    </div>

    <br>
    <br>

    <div class="product-container">

      <div class="card lg:card-side bg-base-100 shadow-xl">
        <figure>
            <img class="mask mask-circle" src="http://localhost:8000/images/{influencer?.name}" alt="ProfilePicture"/>
        </figure>
        <div class="card-body">

            <div style="display: flex;">
                <img src="/instagram.png" alt="instagram" style="width: 20px; height: 20px; margin-right: 5px;"/>
                <h2 class="card-title" style="margin-right: 5px;">{influencer?.name}</h2>
                <h2 class="card-title">({formatFollowersCount(influencer?.ig_followers)} followers)</h2>
            </div>
            <div style="display: flex;">
                <img src="/tiktok.png" alt="tiktok" style="width: 20px; height: 20px; margin-right: 5px;"/>
                <h2 class="card-title" style="margin-right: 5px;">{influencer?.name}</h2>
                <h2 class="card-title">({formatFollowersCount(influencer?.ig_followers)} followers)</h2>
            </div>
          <br>
          <br>
        </div>
      </div>

  </div>

  <article class="prose">
    <h2>Showcased products</h2>
  </article>

  <br>

    <div class="overflow-x-auto">
        <table class="table">
        <thead>
          <tr>
            <th>Product</th>
            <th>Brand</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
        {#each influencer?.top_products || [] as product}
        <tr>
            <td>
                <div class="flex items-center gap-3">
                    <div class="avatar">
                        <div class="mask mask-squircle w-12 h-12">
                            <img class="mask mask-squircle" src={product.image} alt="product"/>
                        </div>
                    </div>
                <div>
                    <div class="font-bold">
                        {product.name}
                    </div>
                </div>
              </div>
            </td>
            <td>
                {product.brand}
            </td>
            <th>
                <a href="/product/{product.id}">
                    <button class="btn btn-ghost btn-xs">details</button>
                </a>
            </th>
        </tr>
        {/each}
        </table>
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
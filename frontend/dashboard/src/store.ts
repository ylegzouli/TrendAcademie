import { writable } from 'svelte/store';

type Influencer = {
    id: string
    name: string
    likes: string
    ig_followers: string
    top_products: any[]
}

export const influencers = writable<Influencer[]>([]);
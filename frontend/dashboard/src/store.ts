import { writable } from 'svelte/store';

type Influencer = {
    id: string
    name: string
    image: string // backend url
    likes: string
    // followers: string // instagram
}

export const influencers = writable([]);
// export const influencers = writable<Influencer[]>([]);
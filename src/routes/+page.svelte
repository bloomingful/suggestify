<script lang="ts">
  import Meta from "$lib/components/meta.svelte";
  import { pageManifests } from "$lib/model/manifests";
  import { isLoading } from "$lib/model/store";
  import { onMount } from "svelte";
  import Coffee from "./coffee.svelte";

  onMount(() => ($isLoading = false));
</script>

<Meta pageManifest={pageManifests.HOME} />
<div class="container">
  <div class="wide-title">
    <p>A svelte project template with<br />sveltekit & Svelte Material UI</p>
  </div>

  <article>
    <Coffee />
  </article>
</div>

<style lang="scss">
  .container {
    .wide-title {
      padding: 30px;
      text-align: center;
      font-weight: 800;
      font-size: 40px;
      line-height: 1.5em;
      color: var(--m3-on-primary-container);
      background-color: var(--m3-inverse-primary);
    }
  }
</style>

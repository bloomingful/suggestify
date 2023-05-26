<script lang="ts">
  import { goto } from "$app/navigation";
  import BackToTop from "$lib/components/back-to-top.svelte";
  import PageTransition from "$lib/components/page-transition.svelte";
  import Splash from "$lib/components/splash.svelte";
  import { isLandscapeDetect } from "$lib/model/constants";
  import { isLandscape, isLoading } from "$lib/model/store";
  import { ThemeProvider } from "$lib/model/theme";
  import Button, { Label } from "@smui/button";
  import { AppContent } from "@smui/drawer";
  import IconButton, { Icon } from "@smui/icon-button";
  import LinearProgress from "@smui/linear-progress";
  import type TopAppBarComponentDev from "@smui/top-app-bar";
  import TopAppBar, {
    AutoAdjust,
    Row,
    Section,
    Title,
  } from "@smui/top-app-bar";
  import { onMount } from "svelte";
  import BookOutline from "svelte-material-icons/BookOutline.svelte";
  import Launch from "svelte-material-icons/Launch.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  let topAppBar: TopAppBarComponentDev;
  let hasMounted = false;

  onMount(() => {
    updateSize();
    hasMounted = true;

    // callback windows width event
    window.addEventListener("resize", updateSize);

    // callback prefers-color-scheme event
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
    prefersDark.addEventListener("change", () => new ThemeProvider().update());
  });

  function updateSize(): void {
    $isLandscape = isLandscapeDetect();
  }
</script>

<div class:isLoading={$isLoading}>
  <TopAppBar bind:this={topAppBar} variant="fixed">
    <Row>
      <Section>
        <IconButton>
          <BookOutline />
        </IconButton>

        <Title style="cursor: pointer;"><strong>tpl-svelte</strong></Title>
      </Section>
      <Section align="end" toolbar>
        <Button
          on:click={() => goto("https://github.com/wappon-28-dev/tpl-svelte")}
        >
          <Icon><Launch /></Icon>
          <Label>source</Label>
        </Button>
      </Section>
    </Row>

    <div class="progress-mobile">
      {#if $isLoading}
        <LinearProgress class="progress-bar-mobile" indeterminate />
      {/if}
    </div>
  </TopAppBar>
  <AutoAdjust {topAppBar}>
    <AppContent class="app-content">
      <PageTransition {data}>
        <slot />
      </PageTransition>
    </AppContent>
  </AutoAdjust>

  <BackToTop />
</div>
<Splash isMounting={!hasMounted} isLoading={$isLoading} />

<style lang="scss">
  :global(.app-content) {
    overflow-y: visible;
    overflow-x: hidden;

    height: 100%;
    width: 100%;

    &.isLoading {
      pointer-events: none;
    }
  }

  :global(
      .mdc-circular-progress__determinate-circle,
      .mdc-circular-progress__indeterminate-circle-graphic
    ) {
    stroke: var(--m3-on-primary);
  }

  .progress-mobile {
    margin-top: -5.5px;
    min-height: 4px;
  }
</style>

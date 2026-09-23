# keremltd

## Status

| | |
|---|---|
| **Domain** | `https://keremltd.co.il` |
| **Pages URL** | `https://keremltd.pages.dev` |
| **Storage mode** | `Standard` (`standard`) |
| **Storage account** | `jetvaults` |
| **Public storage** | `https://jetvaults.blob.core.windows.net/keremltd/` |
| **Private storage** | `https://jetvaults.blob.core.windows.net/keremltd-private/` |
| **Public container** | `keremltd` |
| **Private container** | `keremltd-private` |
| **Activated** | No |

## Nameservers

Set these at your domain registrar:

```
gordon.ns.cloudflare.com
sureena.ns.cloudflare.com
```

## Development

Edit files in `wwwroot/` and push to `main` - Cloudflare Pages auto-deploys.

Only the `wwwroot/` directory is served. Everything else stays in the repo.

## Build

Pages are generated from `tools/build.py` (content + templates, no dependencies):

```
python tools/build.py
```

It rewrites every HTML file under `wwwroot/` and inlines `wwwroot/assets/css/site.css`.
Responsive AVIF/WebP images are produced by `tools/optimize_images.py <source-dir>`
(source originals are not committed; they live on the previous WordPress site).

Contact forms post to Web3Forms. Replace `WEB3FORMS_KEY` in `tools/build.py` and rebuild.

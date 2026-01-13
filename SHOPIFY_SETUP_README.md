# Shopify Product Setup - Memento Mori Garden

Automated Shopify product creation with Gemini AI-generated images.

## Overview

This script automates the entire process of creating the Memento Mori Garden t-shirt product on Shopify, including:
- Generating professional product images using Gemini AI
- Creating product with all color and size variants (56 SKUs total)
- Uploading images to Shopify
- Setting pricing, descriptions, and inventory

## Prerequisites

1. **Python 3.7+** installed
2. **Required Python packages:**
   ```bash
   pip install requests python-dotenv
   ```

3. **API Credentials** (already configured in `.env` file):
   - Shopify API Key and Secret
   - Gemini API Key and Project ID

## Configuration

The script uses environment variables from `.env` file:

```bash
# Shopify Configuration
SHOPIFY_STORE=the-office-9041.myshopify.com
SHOPIFY_API_KEY=your_shopify_api_key
SHOPIFY_API_SECRET=your_shopify_api_secret

# Gemini AI Configuration
GEMINI_API_KEY=your_gemini_api_key
GEMINI_PROJECT_ID=your_gemini_project_id
```

**Note:** The `.env` file is gitignored for security. See `.env.example` for template.

## Usage

### Option 1: Run Locally (Recommended if MCP not available)

Run the script from your local machine where network access isn't restricted:

```bash
python3 shopify_setup.py
```

The script will:
1. ✅ Test API connections (Shopify + Gemini)
2. ✅ Generate 8 product images (one per colorway)
3. ✅ Create main product with 56 variants
4. ✅ Upload all images to Shopify
5. ✅ Set pricing and descriptions
6. ✅ Product created in DRAFT status for review

### Option 2: Use Shopify MCP Server

If you have a Shopify MCP server installed in your Claude Code environment, you can use the native MCP tools instead.

## Product Details

### Main Product
**Title:** Memento Mori Garden - Botanical Skull Art T-Shirt

### Colorways (8)
1. **Midnight Garden (Black)** - $32
2. **Bone Garden (Natural)** - $36
3. **Woodland Memento (Forest Green)** - $34
4. **Gothic Romance (Burgundy)** - $34
5. **Modern Memento (Charcoal)** - $32
6. **Herbalist's Dream (Sage)** - $36
7. **Twilight Bloom (Dusty Rose)** - $34
8. **Midnight Bloom (Navy)** - $32

### Sizes (7)
XS, S, M, L, XL, 2XL, 3XL

### Total Variants
8 colors × 7 sizes = **56 SKUs**

## Generated Images

Images are saved to `generated_images/` directory:
- `memento_mori_black.png`
- `memento_mori_cream.png`
- `memento_mori_forest.png`
- `memento_mori_burgundy.png`
- `memento_mori_charcoal.png`
- `memento_mori_sage.png`
- `memento_mori_mauve.png`
- `memento_mori_navy.png`

## Output

After successful execution, you'll see:
```
============================================================
✓ Product Setup Complete!
============================================================

Product ID: 123456789
Product Title: Memento Mori Garden - Botanical Skull Art T-Shirt
Total Variants: 56
Images Uploaded: 8

Product URL: https://the-office-9041.myshopify.com/admin/products/123456789

⚠ Product is currently in DRAFT status.
   Review and publish when ready!
```

## Next Steps

1. **Review the product** in Shopify admin
2. **Verify images** are correctly associated with colorways
3. **Check pricing** and inventory levels
4. **Publish the product** when ready to go live

## Troubleshooting

### Connection Errors
- Ensure you're running from an environment with network access
- Verify API credentials in `.env` file
- Check Shopify store URL is correct

### Image Generation Fails
- Verify Gemini API key is valid
- Check API quota/limits
- Review Gemini project ID

### Authentication Issues
- Confirm Shopify API secret has proper permissions
- Ensure Admin API access is enabled in Shopify

## API Permissions Required

**Shopify:**
- `write_products` - Create products
- `write_inventory` - Set inventory levels
- `write_product_listings` - Manage product listings

**Gemini:**
- Image generation API access
- Imagen 3.0 model access

## Security Notes

- **Never commit** `.env` file to version control
- API credentials are sensitive - keep them secure
- The script creates products in DRAFT status for review before publishing

## Support

For issues or questions:
- Check Shopify API documentation: https://shopify.dev/docs/api
- Check Gemini AI documentation: https://ai.google.dev/docs
- Review script output for specific error messages

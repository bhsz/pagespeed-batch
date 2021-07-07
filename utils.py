def write_result_html(url, mobile_data, desktop_data):
    # Error
    if ("error" in mobile_data or "error" in desktop_data):
        return f'<!DOCTYPE html><html lang="en"><head><title>{url}</title></head><body><p>{mobile_data["error"]["message"]}</p></body></html>'

    # Headings
    pagespeed_url = f'https://developers.google.com/speed/pagespeed/insights/?url={url.replace("://", "%3A%2F%2F")}'
    result = f'<!DOCTYPE html><html lang="en"><head><title>{url}</title></head><body><h1>Created with PageSpeed Insights API</h1><p>Target URL :{url}</p><a href="{pagespeed_url}">Full PageSpeed Insight here</a><br />'

    # Mobile
    result += "<br />"
    result += f'<h2>Mobile</h2><h3>Performance Score: {mobile_data["lighthouseResult"]["categories"]["performance"]["score"] * 100}</h3>'
    if "metrics" in mobile_data["loadingExperience"]:
        result += f'<h3>Chrome User Experience Results</h3><p>First Contentful Paint (FCP) - {mobile_data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]}ms ({mobile_data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]})</p><p>Largest Contentful Paint (LCP) - {mobile_data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]}ms ({mobile_data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]})</p><p>First Input Delay (FID) - {mobile_data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]}ms ({mobile_data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]})</p><p>Cumulative Layout Shift (CLS) - {mobile_data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"] / 100} ({mobile_data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]})</p>'
    result += f'<h3>Lighthouse Results</h3><p>First Contentful Paint - {mobile_data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]}</p><p>Speed Index - {mobile_data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]}</p><p>Largest Contentful Paint - {mobile_data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]}</p><p>Time To Interactive - {mobile_data["lighthouseResult"]["audits"]["interactive"]["displayValue"]}</p><p>Total Blocking Time - {mobile_data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]}</p><p>Cumulative Layout Shift - {mobile_data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]}</p>'

    # Desktop
    result += "<br />"
    result += f'<h2>Desktop</h2><h3>Performance Score: {desktop_data["lighthouseResult"]["categories"]["performance"]["score"] * 100}</h3>'
    if "metrics" in desktop_data["loadingExperience"]:
        result += f'<h3>Chrome User Experience Results</h3><p>First Contentful Paint (FCP) - {desktop_data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]}ms ({desktop_data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]})</p><p>Largest Contentful Paint (LCP) - {desktop_data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]}ms ({desktop_data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]})</p><p>First Input Delay (FID) - {desktop_data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]}ms ({desktop_data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]})</p><p>Cumulative Layout Shift (CLS) - {desktop_data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"] / 100} ({desktop_data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]})</p>'
    result += f'<h3>Lighthouse Results</h3><p>First Contentful Paint - {desktop_data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]}</p><p>Speed Index - {desktop_data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]}</p><p>Largest Contentful Paint - {desktop_data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]}</p><p>Time To Interactive - {desktop_data["lighthouseResult"]["audits"]["interactive"]["displayValue"]}</p><p>Total Blocking Time - {desktop_data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]}</p><p>Cumulative Layout Shift - {desktop_data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"]}</p>'

    # Closing tags
    result += f'</body></html>'
    return result

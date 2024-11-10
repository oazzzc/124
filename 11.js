let body = $response.body;
if (body) {
    try {
        let json = JSON.parse(body);
        if (json.ad_info || json.promo || json.sponsor || json.campaign_id) {
            body = JSON.stringify({});  // 清空广告内容
        }
    } catch (e) {
        console.log("Ad Filtering Error:", e);
    }
}
$done({ body });

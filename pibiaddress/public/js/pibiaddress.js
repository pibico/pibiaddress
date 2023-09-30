frappe.ui.form.on('Address', {
  refresh: function(frm) {
    frm.add_custom_button('Fetch GeoJSON Location', function() {
      if (frm.doc.address_line1 || frm.doc.city || frm.doc.state || frm.doc.pincode || frm.doc.country) {
        frappe.call({
          method: "pibiaddress.pibiaddress.utils.get_geojson_from_address",
          args: {
            "address_line1": frm.doc.address_line1,
            "city": frm.doc.city,
            "state": frm.doc.state,
            "country": frm.doc.country,
            "pincode": frm.doc.pincode
          },
          callback: function(response) {
            if (response && response.message) {
              let geojson_string = JSON.stringify(response.message);
              frm.set_value("ad_location", geojson_string);
            }
          }
        });
      }
    });
  }
});
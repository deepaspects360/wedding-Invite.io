import re

with open('write_index.py', 'r', encoding='utf-8') as f:
    content = f.read()

gifts_en = """<section id="gifts" class="gifts-section rv">
  <h2 class="gifts-title rv d1">Gifts</h2>
  <p class="gifts-tagline rv d2">
    Your presence is our greatest gift.<br>
    If you wish to bless us further,<br>please find the details below.
  </p>
  <div class="gifts-divider"><span class="gifts-divider-icon"><i class="fas fa-cross"></i></span></div>
  <div class="gifts-grid">

    <!-- Groom Bank -->
    <div class="gift-card rv d1">
      <span class="gift-card-icon"><i class="fas fa-university"></i></span>
      <div class="gift-card-type">Bank Transfer</div>
      <div class="gift-card-name">J. Jacob Israel</div>
      <div class="gift-field">
        <div class="gift-field-label">Bank Name</div>
        <div class="gift-field-value">XXXX Bank &mdash; Placeholder</div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">Account Number</div>
        <div class="gift-field-value">
          <span>XXXX XXXX XXXX 0000</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'XXXXXXXXXXXX0000')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">IFSC Code</div>
        <div class="gift-field-value">XXXX0000000</div>
      </div>
    </div>

    <!-- Bride Bank -->
    <div class="gift-card rv d2">
      <span class="gift-card-icon"><i class="fas fa-university"></i></span>
      <div class="gift-card-type">Bank Transfer</div>
      <div class="gift-card-name">N.S. Dhivya</div>
      <div class="gift-field">
        <div class="gift-field-label">Bank Name</div>
        <div class="gift-field-value">XXXX Bank &mdash; Placeholder</div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">Account Number</div>
        <div class="gift-field-value">
          <span>XXXX XXXX XXXX 0000</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'XXXXXXXXXXXX0000')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">IFSC Code</div>
        <div class="gift-field-value">XXXX0000000</div>
      </div>
    </div>

    <!-- GPay / UPI -->
    <div class="gift-card gpay-card rv d3">
      <span class="gift-card-icon"><i class="fas fa-mobile-screen"></i></span>
      <div class="gift-card-type">GPay &bull; PhonePe &bull; UPI</div>
      <div class="gift-card-name">Instant Transfer</div>
      <div class="gift-field">
        <div class="gift-field-label">UPI ID</div>
        <div class="gift-field-value">
          <span>yourname@upi</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'yourname@upi')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">Mobile (GPay / PhonePe)</div>
        <div class="gift-field-value">
          <span>+91 XXXXX XXXXX</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'+91XXXXXXXXXX')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gpay-qr-placeholder">QR Code<br>Placeholder</div>
    </div>

    <!-- Gift Registry / Wishlist -->
    <div class="gift-card rv d4">
      <span class="gift-card-icon"><i class="fas fa-gift"></i></span>
      <div class="gift-card-type">Gift Wishlist</div>
      <div class="gift-card-name">Registry &amp; Wishlist</div>
      <div class="gift-field">
        <div class="gift-field-label">Amazon Wishlist</div>
        <div class="gift-field-value" style="font-family:sans-serif;font-size:0.78rem;">
          <span>Link coming soon&hellip;</span>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">Gift Card (Amazon)</div>
        <div class="gift-field-value" style="font-family:sans-serif;font-size:0.78rem;">
          <span>jacob.israel@email.com</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'jacob.israel@email.com')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <p style="font-size:0.72rem;color:#a07840;font-family:'Cormorant Garamond',serif;font-style:italic;margin-top:10px;">Send an Amazon / Flipkart gift card to the email above.</p>
    </div>

  </div>
  <p class="gifts-note rv"><i class="fas fa-star" style="font-size:0.8em;color:var(--gold);"></i> Most importantly &mdash; your love, prayers &amp; blessings mean everything to us. <i class="fas fa-star" style="font-size:0.8em;color:var(--gold);"></i></p>
</section>"""

gifts_ta = """<section id="gifts" class="gifts-section rv">
  <h2 class="gifts-title rv d1">
    <span data-lang="en">Gifts</span>
    <span data-lang="ta">\\u0baa\\u0bb0\\u0bbf\\u0b9a\\u0bc1\\u0b95\\u0bb3\\u0bcd</span>
  </h2>
  <p class="gifts-tagline rv d2">
    <span data-lang="en">Your presence is our greatest gift.<br>If you wish to bless us further,<br>please find the details below.</span>
    <span data-lang="ta">\\u0ba4\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bcd \\u0bb5\\u0bb0\\u0bc1\\u0b95\\u0bc8\\u0baf\\u0bc7 \\u0b8e\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bbf\\u0ba9\\u0bcd \\u0bae\\u0bbf\\u0b95\\u0baa\\u0bcd\\u0baa\\u0bc6\\u0bb0\\u0bbf\\u0baf \\u0baa\\u0bb0\\u0bbf\\u0b9a\\u0bc1.<br>\\u0b8e\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bc8 \\u0bae\\u0bc7\\u0bb2\\u0bc1\\u0bae\\u0bcd \\u0b86\\u0b9a\\u0bc0\\u0bb0\\u0bcd\\u0bb5\\u0ba4\\u0bbf\\u0b95\\u0bcd\\u0b95 \\u0bb5\\u0bbf\\u0bb0\\u0bc1\\u0bae\\u0bcd\\u0baa\\u0bbf\\u0ba9\\u0bbe\\u0bb2\\u0bcd,<br>\\u0b95\\u0bc0\\u0bb4\\u0bc7 \\u0b89\\u0bb3\\u0bcd\\u0bb3 \\u0bb5\\u0bbf\\u0bb5\\u0bb0\\u0b95\\u0bcd\\u0b95\\u0bbe\\u0ba3\\u0bb5\\u0bc1\\u0bae\\u0bcd.</span>
  </p>
  <div class="gifts-divider"><span class="gifts-divider-icon"><i class="fas fa-cross"></i></span></div>
  <div class="gifts-grid">

    <!-- Groom Bank -->
    <div class="gift-card rv d1">
      <span class="gift-card-icon"><i class="fas fa-university"></i></span>
      <div class="gift-card-type">
        <span data-lang="en">Bank Transfer</span>
        <span data-lang="ta">\\u0bb5\\u0b99\\u0bcd\\u0b95\\u0bbf \\u0baa\\u0bb0\\u0bbf\\u0bae\\u0bbe\\u0bb1\\u0bcd\\u0bb1\\u0bae\\u0bcd</span>
      </div>
      <div class="gift-card-name">
        <span data-lang="en">J. Jacob Israel</span>
        <span data-lang="ta" style="font-family:'Cormorant Garamond',serif;font-style:italic;">\\u0b9c\\u0bbe. \\u0b9c\\u0bc7\\u0b95\\u0bcd\\u0b95\\u0baa\\u0bcd \\u0b87\\u0bb8\\u0bcd\\u0bb0\\u0bc7\\u0bb2\\u0bcd</span>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Bank Name</span>
          <span data-lang="ta">\\u0bb5\\u0b99\\u0bcd\\u0b95\\u0bbf \\u0baa\\u0bc6\\u0baf\\u0bb0\\u0bcd</span>
        </div>
        <div class="gift-field-value">XXXX Bank &mdash; Placeholder</div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Account Number</span>
          <span data-lang="ta">\\u0b95\\u0ba3\\u0b95\\u0bcd\\u0b95\\u0bc1 \\u0b8e\\u0ba3\\u0bcd</span>
        </div>
        <div class="gift-field-value">
          <span>XXXX XXXX XXXX 0000</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'XXXXXXXXXXXX0000')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">IFSC Code</span>
          <span data-lang="ta">IFSC \\u0b95\\u0bc1\\u0bb1\\u0bbf\\u0baf\\u0bc0\\u0b9f\\u0bc1</span>
        </div>
        <div class="gift-field-value">XXXX0000000</div>
      </div>
    </div>

    <!-- Bride Bank -->
    <div class="gift-card rv d2">
      <span class="gift-card-icon"><i class="fas fa-university"></i></span>
      <div class="gift-card-type">
        <span data-lang="en">Bank Transfer</span>
        <span data-lang="ta">\\u0bb5\\u0b99\\u0bcd\\u0b95\\u0bbf \\u0baa\\u0bb0\\u0bbf\\u0bae\\u0bbe\\u0bb1\\u0bcd\\u0bb1\\u0bae\\u0bcd</span>
      </div>
      <div class="gift-card-name">
        <span data-lang="en">N.S. Dhivya</span>
        <span data-lang="ta" style="font-family:'Cormorant Garamond',serif;font-style:italic;">\\u0b8e\\u0ba9\\u0bcd.\\u0b9a\\u0bbf. \\u0ba4\\u0bbf\\u0baf\\u0bbe</span>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Bank Name</span>
          <span data-lang="ta">\\u0bb5\\u0b99\\u0bcd\\u0b95\\u0bbf \\u0baa\\u0bc6\\u0baf\\u0bb0\\u0bcd</span>
        </div>
        <div class="gift-field-value">XXXX Bank &mdash; Placeholder</div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Account Number</span>
          <span data-lang="ta">\\u0b95\\u0ba3\\u0b95\\u0bcd\\u0b95\\u0bc1 \\u0b8e\\u0ba3\\u0bcd</span>
        </div>
        <div class="gift-field-value">
          <span>XXXX XXXX XXXX 0000</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'XXXXXXXXXXXX0000')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">IFSC Code</span>
          <span data-lang="ta">IFSC \\u0b95\\u0bc1\\u0bb1\\u0bbf\\u0baf\\u0bc0\\u0b9f\\u0bc1</span>
        </div>
        <div class="gift-field-value">XXXX0000000</div>
      </div>
    </div>

    <!-- GPay / UPI -->
    <div class="gift-card gpay-card rv d3">
      <span class="gift-card-icon"><i class="fas fa-mobile-screen"></i></span>
      <div class="gift-card-type">GPay &bull; PhonePe &bull; UPI</div>
      <div class="gift-card-name">
        <span data-lang="en">Instant Transfer</span>
        <span data-lang="ta">\\u0b89\\u0b9f\\u0ba9\\u0b9f\\u0bbf \\u0baa\\u0bb0\\u0bbf\\u0bae\\u0bbe\\u0bb1\\u0bcd\\u0bb1\\u0bae\\u0bcd</span>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">UPI ID</span>
          <span data-lang="ta">UPI \\u0b90\\u0b9f\\u0bbf</span>
        </div>
        <div class="gift-field-value">
          <span>yourname@upi</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'yourname@upi')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Mobile (GPay / PhonePe)</span>
          <span data-lang="ta">\\u0bae\\u0bca\\u0baa\\u0bc8\\u0bb2\\u0bcd (GPay / PhonePe)</span>
        </div>
        <div class="gift-field-value">
          <span>+91 XXXXX XXXXX</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'+91XXXXXXXXXX')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <div class="gpay-qr-placeholder">
        <span data-lang="en">QR Code<br>Placeholder</span>
        <span data-lang="ta">QR \\u0b95\\u0bc1\\u0bb1\\u0bbf\\u0baf\\u0bc0\\u0b9f\\u0bc1<br>\\u0b87\\u0b9f\\u0bae\\u0bcd</span>
      </div>
    </div>

    <!-- Gift Registry / Wishlist -->
    <div class="gift-card rv d4">
      <span class="gift-card-icon"><i class="fas fa-gift"></i></span>
      <div class="gift-card-type">
        <span data-lang="en">Gift Wishlist</span>
        <span data-lang="ta">\\u0baa\\u0bb0\\u0bbf\\u0b9a\\u0bc1 \\u0bb5\\u0bbf\\u0bb0\\u0bc1\\u0baa\\u0bcd\\u0baa\\u0baa\\u0bcd\\u0baa\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0baf\\u0bb2\\u0bcd</span>
      </div>
      <div class="gift-card-name">
        <span data-lang="en">Registry &amp; Wishlist</span>
        <span data-lang="ta">\\u0bb5\\u0bbf\\u0bb0\\u0bc1\\u0baa\\u0bcd\\u0baa\\u0baa\\u0bcd\\u0baa\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0baf\\u0bb2\\u0bcd</span>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Amazon Wishlist</span>
          <span data-lang="ta">\\u0b85\\u0bae\\u0bc7\\u0b9a\\u0bbe\\u0ba9\\u0bcd \\u0bb5\\u0bbf\\u0bb0\\u0bc1\\u0baa\\u0bcd\\u0baa\\u0baa\\u0bcd\\u0baa\\u0b9f\\u0bcd\\u0b9f\\u0bbf\\u0baf\\u0bb2\\u0bcd</span>
        </div>
        <div class="gift-field-value" style="font-family:sans-serif;font-size:0.78rem;">
          <span data-lang="en">Link coming soon&hellip;</span>
          <span data-lang="ta">\\u0bb5\\u0bbf\\u0bb0\\u0bc8\\u0bb5\\u0bbf\\u0bb2\\u0bcd&hellip;</span>
        </div>
      </div>
      <div class="gift-field">
        <div class="gift-field-label">
          <span data-lang="en">Gift Card (Amazon)</span>
          <span data-lang="ta">\\u0baa\\u0bb0\\u0bbf\\u0b9a\\u0bc1 \\u0b85\\u0b9f\\u0bcd\\u0b9f\\u0bc8 (Amazon)</span>
        </div>
        <div class="gift-field-value" style="font-family:sans-serif;font-size:0.78rem;">
          <span>jacob.israel@email.com</span>
          <button class="gift-copy-btn" onclick="copyGift(this,'jacob.israel@email.com')" title="Copy"><i class="far fa-copy"></i></button>
        </div>
      </div>
      <p style="font-size:0.72rem;color:#a07840;font-family:'Cormorant Garamond',serif;font-style:italic;margin-top:10px;">
        <span data-lang="en">Send an Amazon / Flipkart gift card to the email above.</span>
        <span data-lang="ta">\\u0bae\\u0bc7\\u0bb1\\u0bcd\\u0b95\\u0ba3\\u0bcd\\u0b9f \\u0bae\\u0bbf\\u0ba9\\u0bcd\\u0ba9\\u0b9e\\u0bcd\\u0b9a\\u0bb2\\u0bc1\\u0b95\\u0bcd\\u0b95\\u0bc1 \\u0b85\\u0bae\\u0bc7\\u0b9a\\u0bbe\\u0ba9\\u0bcd / \\u0baa\\u0bbf\\u0bb3\\u0bbf\\u0baa\\u0bcd\\u0b95\\u0bbe\\u0bb0\\u0bcd\\u0b9f\\u0bcd \\u0baa\\u0bb0\\u0bbf\\u0b9a\\u0bc1 \\u0b85\\u0b9f\\u0bcd\\u0b9f\\u0bc8\\u0baf\\u0bc8 \\u0b85\\u0ba9\\u0bc1\\u0baa\\u0bcd\\u0baa\\u0bb5\\u0bc1\\u0bae\\u0bcd.</span>
      </p>
    </div>

  </div>
  <p class="gifts-note rv">
    <i class="fas fa-star" style="font-size:0.8em;color:var(--gold);"></i> 
    <span data-lang="en">Most importantly &mdash; your love, prayers &amp; blessings mean everything to us.</span>
    <span data-lang="ta">\\u0bae\\u0bbf\\u0b95 \\u0bae\\u0bc1\\u0b95\\u0bcd\\u0b95\\u0bbf\\u0baf\\u0bae\\u0bbe\\u0b95 &mdash; \\u0b89\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bcd \\u0b85\\u0ba9\\u0bcd\\u0baa\\u0bc1, \\u0baa\\u0bbf\\u0bb0\\u0bbe\\u0bb0\\u0bcd\\u0ba4\\u0bcd\\u0ba4\\u0ba9\\u0bc8 \\u0bae\\u0bb1\\u0bcd\\u0bb1\\u0bc1\\u0bae\\u0bcd \\u0b86\\u0b9a\\u0bc0\\u0bb0\\u0bcd\\u0bb5\\u0bbe\\u0ba4\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bcd \\u0b8e\\u0b99\\u0bcd\\u0b95\\u0bb3\\u0bc1\\u0b95\\u0bcd\\u0b95\\u0bc1 \\u0bae\\u0bbf\\u0b95\\u0bb5\\u0bc1\\u0bae\\u0bcd \\u0bb5\\u0bbf\\u0bb2\\u0bc8\\u0bae\\u0ba4\\u0bbf\\u0baa\\u0bcd\\u0baa\\u0bb1\\u0bcd\\u0bb1\\u0bb5\\u0bc8.</span> 
    <i class="fas fa-star" style="font-size:0.8em;color:var(--gold);"></i>
  </p>
</section>"""

if gifts_en in content:
    new_content = content.replace(gifts_en, gifts_ta)
    with open('write_index.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find the target content.")

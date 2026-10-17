import re

with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()

# Replace modalCreateMatch form and HTML
old_modal_html = re.search(r'<!-- CREATE CUSTOM MATCH BOTTOM SHEET -->.*?</form>\s*</div>\s*</div>', idx, re.DOTALL)

new_modal_html = """  <!-- CREATE CUSTOM MATCH BOTTOM SHEET -->
  <div class="modal-backdrop" id="modalCreateMatch">
    <div class="bottom-sheet" style="max-height:92vh; overflow-y:auto; padding-bottom: calc(24px + env(safe-area-inset-bottom, 0px));">
      <div class="sheet-handle"></div>
      <div class="sheet-header">
        <div class="sheet-title"><i class="fa-solid fa-plus-circle" style="color:var(--neon-cyan);"></i> Create Your Match</div>
        <button class="btn-close-sheet" onclick="closeModal('modalCreateMatch')">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <form id="createMatchForm" onsubmit="submitCreateCustomMatch(event)">
        
        <!-- 1. Room Mode -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Room Mode</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn active" id="modeClashSquad" onclick="setCreateMatchMode('Clash Squad')">Clash Squad</button>
            <button type="button" class="seg-btn" id="modeLoneWolf" onclick="setCreateMatchMode('Lone Wolf')">Lone Wolf</button>
          </div>
          <input type="hidden" id="cmRoomMode" value="Clash Squad">
        </div>

        <!-- 2. Player Format -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Player Format</label>
          <div style="display:flex; gap:6px;" id="cmPlayerFormatsRow">
            <!-- Populated dynamically -->
          </div>
          <input type="hidden" id="cmPlayerFormat" value="1v1">
        </div>

        <!-- 3. Limited Ammo -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Limited Ammo</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn" id="ammoYes" onclick="setSeg('cmLimitedAmmo', 'Yes')">Yes</button>
            <button type="button" class="seg-btn active" id="ammoNo" onclick="setSeg('cmLimitedAmmo', 'No')">No</button>
          </div>
          <input type="hidden" id="cmLimitedAmmo" value="No">
        </div>

        <!-- 4. Gun Attribute (Clash Squad only) -->
        <div style="margin-bottom:14px;" id="groupGunAttr">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Gun Attribute</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn" id="gunAttrYes" onclick="setSeg('cmGunAttribute', 'Yes')">Yes</button>
            <button type="button" class="seg-btn active" id="gunAttrNo" onclick="setSeg('cmGunAttribute', 'No')">No</button>
          </div>
          <input type="hidden" id="cmGunAttribute" value="No">
        </div>

        <!-- 5. Headshot -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Headshot Only</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn" id="hsYes" onclick="setSeg('cmHeadshot', 'Yes')">Yes</button>
            <button type="button" class="seg-btn active" id="hsNo" onclick="setSeg('cmHeadshot', 'No')">No</button>
          </div>
          <input type="hidden" id="cmHeadshot" value="No">
        </div>

        <!-- 6. Character Skill -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Character Skill</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn" id="skillYes" onclick="setSeg('cmCharacterSkill', 'Yes')">Yes</button>
            <button type="button" class="seg-btn active" id="skillNo" onclick="setSeg('cmCharacterSkill', 'No')">No</button>
          </div>
          <input type="hidden" id="cmCharacterSkill" value="No">
        </div>

        <!-- 7. Game Items Mode (Clash Squad only) -->
        <div style="margin-bottom:14px;" id="groupItemsMode">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Game Items Mode</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn active" id="itemsCompulsory" onclick="setSeg('cmItemsMode', 'Compulsory')">Compulsory</button>
            <button type="button" class="seg-btn" id="itemsSelect" onclick="setSeg('cmItemsMode', 'Select Items')">Select Items</button>
          </div>
          <input type="hidden" id="cmItemsMode" value="Compulsory">
        </div>

        <!-- 8. Rounds -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Rounds</label>
          <div style="display:flex; gap:6px;">
            <button type="button" class="seg-btn" id="round7" onclick="setSeg('cmRounds', '7')">7</button>
            <button type="button" class="seg-btn" id="round9" onclick="setSeg('cmRounds', '9')">9</button>
            <button type="button" class="seg-btn" id="round13" onclick="setSeg('cmRounds', '13')">13</button>
            <button type="button" class="seg-btn active" id="round15" onclick="setSeg('cmRounds', '15')">15</button>
          </div>
          <input type="hidden" id="cmRounds" value="15">
        </div>

        <!-- 9. Coin (Clash Squad only) -->
        <div style="margin-bottom:14px;" id="groupCoinMode">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Coin</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="seg-btn active" id="coinDefault" onclick="setSeg('cmCoinMode', 'Default')">Default</button>
            <button type="button" class="seg-btn" id="coin9999" onclick="setSeg('cmCoinMode', '9999')">9999</button>
          </div>
          <input type="hidden" id="cmCoinMode" value="Default">
        </div>

        <!-- 10. Game Name & UID -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:4px;">In-Game Name * (max 30 chars)</label>
          <input type="text" id="cmGameName" class="form-input" maxlength="30" placeholder="Your in-game name" required oninput="validateCreateMatchForm()" style="width:100%; padding:10px; background:var(--bg-card); border:1px solid var(--surface-border); border-radius:8px; color:#fff;">
          <div style="font-size:11px; color:var(--neon-cyan); margin-top:3px;" id="cmHostUidDisplay">Free Fire UID: --</div>
          <div id="cmNameError" style="font-size:10px; color:var(--neon-red); margin-top:2px; display:none;">In-game name required (max 30 chars).</div>
        </div>

        <!-- 11. Points (Stake) -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:4px;">Points (Stake per side, min 10) *</label>
          <input type="number" id="cmPoints" class="form-input" min="10" max="1000" value="50" oninput="updateCreateMatchSummary(); validateCreateMatchForm();" required style="width:100%; padding:10px; background:var(--bg-card); border:1px solid var(--surface-border); border-radius:8px; color:#fff;">
          <div id="cmPointsError" style="font-size:10px; color:var(--neon-red); margin-top:2px; display:none;">Points must be between 10 and 1000.</div>
        </div>

        <!-- 12. Match Time -->
        <div style="margin-bottom:14px;">
          <label style="font-size:12px; color:var(--text-secondary); display:block; margin-bottom:6px;">Match Time *</label>
          <div style="display:flex; gap:6px; margin-bottom:8px; flex-wrap:wrap;">
            <button type="button" class="seg-btn" onclick="setMatchTimeQuick(30)">In 30 min</button>
            <button type="button" class="seg-btn" onclick="setMatchTimeQuick(60)">In 1 hour</button>
            <button type="button" class="seg-btn" onclick="setMatchTimeQuick(120)">In 2 hours</button>
            <button type="button" class="seg-btn active" onclick="toggleCustomTimeInput()">Custom</button>
          </div>
          <div id="cmCustomTimeWrap">
            <input type="datetime-local" id="cmDateTime" class="form-input" onchange="validateCreateMatchForm()" style="width:100%; padding:10px; background:var(--bg-card); border:1px solid var(--surface-border); border-radius:8px; color:#fff;">
          </div>
          <div id="cmTimePreview" style="font-size:11px; color:var(--neon-cyan); margin-top:4px;">Select start time (30 min to 7 days ahead)</div>
        </div>

        <!-- 13. Prize Preview Card -->
        <div style="background:rgba(0,229,255,0.06); border:1px solid rgba(0,229,255,0.3); border-radius:10px; padding:12px; margin-bottom:14px; font-size:12px; color:#fff; line-height:1.5;" id="cmPrizePreviewCard">
          Stake per side: 50 | Total pool: 100 | Platform fee 10%: 5 | Winner gets: 95
        </div>

        <!-- 14. Rules & Acceptance -->
        <div style="background:rgba(255,152,0,0.08); border:1px solid rgba(255,152,0,0.3); border-radius:10px; padding:12px; margin-bottom:14px;">
          <div style="font-size:12px; color:#fff; margin-bottom:8px;"><i class="fa-solid fa-triangle-exclamation" style="color:var(--neon-amber);"></i> Please read the rules and regulations before creating a match.</div>
          <button type="button" class="btn btn-secondary" onclick="openMatchRulesSheet()" style="padding:6px 12px; font-size:11px; margin-bottom:8px; background:rgba(0,229,255,0.15); color:var(--neon-cyan); border-color:rgba(0,229,255,0.3);">
            View <span id="cmRulesBtnLabel">Clash Squad</span> Rules
          </button>
          <div style="display:flex; align-items:flex-start; gap:8px; margin-top:6px;">
            <input type="checkbox" id="cmRulesCheckbox" onchange="validateCreateMatchForm()" style="margin-top:2px; width:16px; height:16px; accent-color:var(--neon-cyan);">
            <label for="cmRulesCheckbox" style="font-size:11px; color:#fff; cursor:pointer; line-height:1.3;">I have read and accept the rules</label>
          </div>
        </div>

        <!-- 15. Sticky Publish Button -->
        <div style="position:sticky; bottom:0; background:var(--bg-dark); padding:10px 0 0 0; border-top:1px solid var(--surface-border); z-index:5;">
          <button type="submit" id="cmPublishBtn" class="btn btn-primary" disabled style="width:100%; justify-content:center; padding:12px; font-weight:700; opacity:0.5;">
            <i class="fa-solid fa-rocket"></i> Publish Match (Pending Approval)
          </button>
        </div>

      </form>
    </div>
  </div>"""

if old_modal_html:
    idx = idx.replace(old_modal_html.group(0), new_modal_html)
    print("Replaced modalCreateMatch HTML")
else:
    print("Warning: modalCreateMatch HTML not found")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx)

print("index.html create match form HTML updated.")

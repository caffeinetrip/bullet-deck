#version 330

uniform sampler2D surface;
uniform sampler2D ui_surf;
uniform sampler2D light_surf;
uniform sampler2D background_surf;

out vec4 f_color;
in vec2 uv;

const vec3 color_ramp[4] = vec3[4](vec3(40 / 255.0, 35 / 255.0, 40 / 255.0), vec3(84 / 255.0, 92 / 255.0, 126 / 255.0), vec3(197 / 255.0, 105 / 255.0, 129 / 255.0), vec3(163 / 255.0, 162 / 255.0, 154 / 255.0));

void main() {
  vec3 bg_color = texture(background_surf, uv).rgb;

  f_color = vec4(bg_color, 1.0);


  vec4 src_color = texture(surface, uv);

  if (src_color.a > 0.5) {
    int color_i = 0;
    for (int i = 0; i < 4; i++) {
      if (length(color_ramp[i] - src_color.rgb) < (5 / 255.0)) {
        color_i = i;
      }
    }

    int light_color = int(texture(light_surf, uv).r * 255.0 / 10.0);

    color_i = max(0, color_i - (3 - light_color));

    f_color = vec4(color_ramp[color_i], 1.0);
  }

  vec4 ui_color = texture(ui_surf, uv);
  if (ui_color.a > 0) {
    f_color = ui_color;
  }
}
ARCH_FLAGS=-arch arm64 -arch armv7s -arch armv7s
SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/
MINIOS=10.0
SOURCES:=$(shell find . -name '*.c')
CFLAGS=-I .
LDFLAGS=-framework IOKit

default: get_bag1 list-identities

get_bag1: $(SOURCES)
	clang $(ARCH_FLAGS) -isysroot $(SDKROOT) -miphoneos-version-min=$(MINIOS) $(CFLAGS) $(LDFLAGS) $(SOURCES) -o get_bag1

list-identities:
	security find-identity -pcodesigning
	@printf '\nTo codesign, please run: \n\tCER="<40 character hex string for certificate>" make codesign\n'

codesign:
	codesign -fs "$(CER)" --entitlements entitlements.xml get_bag1

gen-parser: keybag.ksy
	kaitai-struct-compiler -t python keybag.ksy

clean:
	rm get_bag1
